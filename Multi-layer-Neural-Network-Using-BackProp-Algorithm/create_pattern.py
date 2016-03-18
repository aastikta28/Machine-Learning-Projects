# -*- coding: utf-8 -*-
import attribute

def pattern(data, atr_list, target_attr):
    pat = []    
    
    mydict = {}

    for attr in atr_list:
        prob = 1.0/int(attribute.Attribute.getvals(attr)[2])
        vals = attribute.Attribute.getvals(attr)[3]
        val = prob            
        for v in vals:
            mydict[v] = val
            val = val + prob
    
    t_prob = 1.0/int(attribute.Attribute.getvals(target_attr)[2])
    t_vals = attribute.Attribute.getvals(target_attr)[3]
    val = t_prob
    for v in t_vals:
        mydict[v] = val
        val = val + t_prob
            
    for d in data:
        p = []
        target = d[-1]
        del d[-1]
        for val in d:
            p.append(mydict[val])
        op = []
        for t in t_vals:
            if t == target:            
                op.append(1.0)
            else:
                op.append(0.0)
        new_p = []
        new_p.append(p)
        new_p.append(op)
        pat.append(new_p)
    
     
#    for p in pat:
#        print p
    return pat