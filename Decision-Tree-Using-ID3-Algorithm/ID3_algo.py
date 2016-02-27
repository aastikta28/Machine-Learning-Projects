# -*- coding: utf-8 -*-
import attribute
import math
import decision_tree
import preprocess

#find most common value for an attribute
def majority(attributes, data, target):
    #find target attribute
    valFreq = {}
    #find target in data
    index = int(attribute.Attribute.getvals(target)[0])-1
    #calculate frequency of values in target attr
    for entry in data:
        if (valFreq.has_key(entry[index])):
            valFreq[entry[index]] += 1 
        else:
            valFreq[entry[index]] = 1
    maxm = 0
    major = ""
    for key in valFreq.keys():
        if valFreq[key]>maxm:
            maxm = valFreq[key]
            major = key
    return major

#Calculates the entropy of the given data set for the target attr
def entropy(attributes, data, target):

    valFreq = {}
    dataEntropy = 0.0
    
    #find index of the target attribute
    i = int(attribute.Attribute.getvals(target)[0])-1
    
    # Calculate the frequency of each of the values in the target attr
    for entry in data:
        if (valFreq.has_key(entry[i])):
            valFreq[entry[i]] += 1.0
        else:
            valFreq[entry[i]]  = 1.0

    # Calculate the entropy of the data for the target attr
    for freq in valFreq.values():
        dataEntropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
        
    return dataEntropy

def information_gain(attributes, data, attr, target_attribute):
    """
    Calculates the information gain (reduction in entropy) that would
    result by splitting the data on the chosen attribute (attr).
    """
    valFreq = {}
    subsetEntropy = 0.0
    
    #find index of the attribute
    i = int(attribute.Attribute.getvals(attr)[0])-1

    # Calculate the frequency of each of the values in the current attribute
    for entry in data:
        if (valFreq.has_key(entry[i])):
            valFreq[entry[i]] += 1.0
        else:
            valFreq[entry[i]]  = 1.0
    # Calculate the sum of the entropy for each subset of records weighted
    # by their probability of occuring in the training set.
    for val in valFreq.keys():
        valProb        = valFreq[val] / sum(valFreq.values())
        dataSubset     = [entry for entry in data if entry[i] == val]
        subsetEntropy += valProb * entropy(attributes, dataSubset, target_attribute)

    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    return (entropy(attributes, data, target_attribute) - subsetEntropy)

def choose_best_attribute(data, attributes, target_attribute):
    best = attributes[0]
    maxGain = 0;
    for attr in attributes:
        newGain = information_gain(attributes, data, attr, target_attribute) 
        if newGain>maxGain:
            maxGain = newGain
            best = attr
    return best

#get values in the column of the given attribute 
def getValues(data, attributes, attr):
    index = int(attribute.Attribute.getvals(attr)[0])-1
    values = []
    for entry in data:
        if entry[index] not in values:
            values.append(entry[index])
    return values

#get all data related to best attribute's value
def getExamples(data, attributes, best, val):
    examples = [[]]
    index = int(attribute.Attribute.getvals(best)[0])-1
    for entry in data:
        #find entries with the given value
        if (entry[index] == val):
            newEntry = []
            #add value if it is not in best column
            for i in range(0,len(entry)):
                newEntry.append(entry[i])
            examples.append(newEntry)
    examples.remove([])
    return examples

#tocheck if all the values belong to + category.
def pos_check(data, attr):
    
    valFreq = {}
    #find index of the attribute
    i = int(attribute.Attribute.getvals(attr)[0])-1

    # Calculate the frequency of each of the values in the target attribute
    for entry in data:
        if (valFreq.has_key(entry[i])):
            valFreq[entry[i]] += 1.0
        else:
            valFreq[entry[i]]  = 1.0

    if len(valFreq.keys()) == 1:
        if valFreq.values() == attribute.Attribute.getvals(attr)[3][0]:
            return True
            
    return False
    
#tocheck if all the values belong to - category.
def neg_check(data, attr):
    
    valFreq = {}
    #find index of the attribute
    i = int(attribute.Attribute.getvals(attr)[0])-1

    # Calculate the frequency of each of the values in the target attribute
    for entry in data:
        if (valFreq.has_key(entry[i])):
            valFreq[entry[i]] += 1.0
        else:
            valFreq[entry[i]]  = 1.0
    
    if len(valFreq.keys()) == 1:
        if valFreq.values() == attribute.Attribute.getvals(attr)[3][1]:
            return True
            
    return False    
  
def check_polarity(target,data):
    valFreq = preprocess.preprocess_discrete(attribute.Attribute.getvals(target)[0],data)
    if len(valFreq) == 1:
        return True
    else:
        return False
  
#main ID3 recursive algorithm
def ID3_algorithm(data, attributes, target_attribute, recursion):
    
    #Number of calls to the function
    recursion += 1
    # creating an empty root node.    
    root = decision_tree.Node() 
    #finding the majority value in data.
    default = majority(attributes, data, target_attribute)
    #checking if all the values are positive.
    if pos_check(data, target_attribute) == True:
        return root.set_values(attribute.Attribute.getvals(target_attribute)[3][0])
    #checking if all the values are negative.
    elif neg_check(data, target_attribute) == True:
        return root.set_values(attribute.Attribute.getvals(target_attribute)[3][1])
    elif len(attributes) <= 0:
        return root.set_values(default)
    else:
        # Choose the next best attribute to best classify our data
        best = choose_best_attribute(data, attributes, target_attribute)
        root.set_values(attribute.Attribute.getvals(best)[1])
        for val in getValues(data, attributes, best):
            # Create a subtree for the current value under the "best" field
            examples = getExamples(data, attributes, best, val)
            if len(examples) <= 0:
                return root.set_values(default)
            else:
                newAttr = attributes[:]
                newAttr.remove(best)
                if(check_polarity(target_attribute,examples) == True):
                    subtree = None
                else:
                    subtree = ID3_algorithm(examples, newAttr, target_attribute, recursion)
                root.set_children(subtree, val, attribute.Attribute.getvals(best)[1],examples)
    
    return root