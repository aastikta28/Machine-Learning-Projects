# -*- coding: utf-8 -*-
import decision_tree

def size(tree,sz):
    if tree == None:
        return sz
    vals = decision_tree.Node.get_values(tree)
    for key,val in vals.items():
        for k,v in val.items():
            sz += 1
            #print "new sz ", sz
            for sub,dat in v.items():
                sz = size(sub,sz)
    return sz