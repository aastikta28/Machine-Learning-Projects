# -*- coding: utf-8 -*-

#attribute class to store all the details of all the attributes in a file.
class Attribute(object):
    def __init__(self, num,name, num_of_vals):
        self.num = num
        self.name = name
        self.num_of_vals = num_of_vals
        self.vals = []
        
    def adding_values(self, val):
        self.vals.append(val)
        
    def printvals(self):
        print self.num, self.name, self.num_of_vals, self.vals
        
    def getvals(self):
        return [self.num, self.name, self.num_of_vals, self.vals]