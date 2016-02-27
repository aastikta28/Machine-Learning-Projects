# -*- coding: utf-8 -*-

import decision_tree
import preprocess

def print_tree(root,attr):
    pretty(root,0,0,attr)
        
def pretty(root, indent, depth, attr):
    if root is None:
        return
    root = decision_tree.Node.get_values(root)
    for key, value in root.items():
        for k,v in value.items():
            print '\t' * indent ,
            print key , "=" ,
            print k , 
            print " [ " ,
            for p,q in v.items():
                freq = preprocess.preprocess_discrete(attr, q)
                for x,y in freq.iteritems():
                    print x , "  : " , y ,
                print " ] "                     
                pretty(p,indent+1,depth+1,attr)
                
    return
       