# -*- coding: utf-8 -*-

def preprocess_discrete(attr, data):
    i = int(attr)-1  
    valFreq = {}
    for entry in data:
        if (valFreq.has_key(entry[i])):
            valFreq[entry[i]] += 1.0
        else:
            valFreq[entry[i]]  = 1.0
    return valFreq
