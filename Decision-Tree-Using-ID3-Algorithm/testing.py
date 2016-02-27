# -*- coding: utf-8 -*-
import decision_tree
import attribute
import preprocess
import math

def testing(tree, data, attr_list, target_attr):
    count = 0
    results = []
    for entry in data:
        #print "testing data: ", entry
        count += 1
        tempDict = decision_tree.Node.get_values(tree)
        result = ""
        while(isinstance(tempDict, dict) and bool(tempDict) is True):
            key = tempDict.keys()[0]
            val = tempDict[key]
            #tempDict = tempDict[key][tempDict[key]][tempDict[key][tempDict[key]]]
            #index = attr_list.index(key)
            index = int(find_index(key, attr_list))-1
            value = entry[index]
            #print key, " and " , value
            #val_chk = val.items()
            if(value in val.keys()):
                #print "inside"
                #child = decision_tree.Node.get_values(value)
                result = val[value]
                for k in result.keys():
                    if k is None:
                        label = find_label(target_attr, result[k])
                        if label == entry[len(entry)-1]:
                            results.append(1)
                            #print "appending"
                        else:
                            results.append(0)
                        tempDict = {}
                    else:
                        tempDict = decision_tree.Node.get_values(k)
            else:
                lb = find_class_label(target_attr,val)
                #print lb
                if lb == entry[len(entry)-1]:
                    results.append(1)
                else:
                    results.append(0)
                break
        #print ("entry%s = %s" % (count, result))
        
    chk = 0.0
    tot_data = len(data)
    for res in results:
        if res is 1:
            chk += res
    #print "tot_data", tot_data
    #correct = chk
    accuracy = chk/tot_data
    errors = tot_data - chk
    stnd_error = math.sqrt(errors*accuracy)
    #print "stnd error: ", stnd_error
    #print "accuracy is", accuracy
    ans = []    
    ans.append(accuracy)
    ans.append(stnd_error)
    return ans
    
def find_index(key, attr_list):
    for a in attr_list:
        if key is attribute.Attribute.getvals(a)[1]:
            return attribute.Attribute.getvals(a)[0]
            
def find_label(target_attr, data):
    freq = preprocess.preprocess_discrete(target_attr.getvals()[0], data)
    maxm = 0
    val = ""
    for x,y in freq.iteritems():
        if y > maxm:
            val = x
    
    #print "label returned ", val
    return val
    
def find_class_label(target_attr,val):
    labels = {}
    for k,v in val.items():
        for k1,v1 in v.items():
            if (labels.has_key(find_label(target_attr,v1))):
                labels[find_label(target_attr,v1)] += 1.0
            else:
                labels[find_label(target_attr,v1)]  = 1.0
            
    maxm = 0
    value = ""
    for k,v in labels.items():
        if maxm < v:
            maxm = v
            value = k
    
    return value