# -*- coding: utf-8 -*-
import decision_tree
import preprocess
    
 
    
def prune_tree(root, tot_data, target_attr):
    if root is None:
        return root
    # finding R(t) for all the subtrees of current node.    
    subtrees = find_all_subtree(root,{},tot_data, target_attr)
    
    # finding leaves attached to the subtrees found above.    
    store_N_for_each_subtree = {}
    
    #finding R(T) if the tree below is not pruned.
    store_R_T_for_each_subtree = {}
    
    #storing alpha for every subtree.
    alpha = {}
    
    for subtree,r in subtrees.items():
        if subtree is not None:
            #print "error cost " , r
            N_T = find_num_of_leaves(subtree,0)
            #print "Number of leaf nodes ", N_T
            store_N_for_each_subtree[subtree] = N_T
            subtree_cost = find_error_cost_of_subtree(subtree,0,tot_data, target_attr)
            #print "error cost if subtree is not pruned ", subtree_cost        
            store_R_T_for_each_subtree[subtree] = subtree_cost
            if N_T is 1:
                alpha[subtree] = 0
            else:
                #print "alpha ", (r - subtree_cost)/(N_T - 1)
                alpha[subtree] = (r - subtree_cost)/(N_T - 1)

       
    if alpha:
        min_value = min(x for x in alpha if x is not None)
        decision_tree.Node.delete_node(min_value)
    
      
    #minm_alpha = min(alpha, key=alpha.get)   
    
    return root
    
    
def find_error_cost_of_subtree(subtree, cost,tot_data, target_attr):
    if subtree is None:
        return cost
    vals = decision_tree.Node.get_values(subtree)
    for key, value in vals.items():
        for k,v in value.items():
            for p,q in v.items():
                if p is None:
                    return cost + find_error_cost(subtree, tot_data, target_attr) 
                else:
                    cost = find_error_cost_of_subtree(p,cost,tot_data,target_attr)
    
    return cost

def find_num_of_leaves(subtree, leaf_count):
    if subtree is None:
        return 0
    vals = decision_tree.Node.get_values(subtree)
    for key, value in vals.items():
        for k,v in value.items():
            for p,q in v.items():
                if p is None:
                    return leaf_count+1
                else:
                    #print p
                    leaf_count = find_num_of_leaves(p,leaf_count)
            #print "count ", leaf_count
    
    return leaf_count
    
def find_all_subtree(root,subtrees,tot_data, target_attr):
    if root is None:
        return subtrees
    root_vals = decision_tree.Node.get_values(root)
    for key, value in root_vals.items():
        for k,v in value.items():
            for p,q in v.items():
                subtrees[p] = find_error_cost(p, tot_data, target_attr)
                
    return subtrees
    
def find_error_cost(subtree, tot_data, target_attr):
    if subtree is None:
        return 0
    subtree_vals = decision_tree.Node.get_values(subtree)
    maxm = 0 
    tot_vals = 0
    wrong_vals = 0
    for key, value in subtree_vals.items():
        for k,v in value.items():
            for p,q in v.items():
                freq = preprocess.preprocess_discrete(target_attr, q)
                for x,y in freq.iteritems():
                    tot_vals += y
                    if y > maxm:
                        wrong_vals += maxm
                        maxm = y
                        #maxm_val = x
                    else:
                        wrong_vals += y 
    
    #print "wrong vals" , wrong_vals
    #print "total vals", tot_vals
    if tot_vals is wrong_vals:
        return 1
    error_rate = (wrong_vals/tot_vals)
    proportion_of_data = (tot_vals)/len(tot_data)
    return (error_rate * proportion_of_data)
    