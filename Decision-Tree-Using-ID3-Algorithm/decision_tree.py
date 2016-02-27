# -*- coding: utf-8 -*-
import copy

class Node(object): 
    
    def __init__(self):
        self.name = {}
        
    def set_values(self, name):
        self.name = {name : {}}
        
    def get_values(self):
        return self.name
        
    def set_children(self, child, val, best,data):
        self.name[best][val] = {child : data}
        
    def delete_node(self):
        self.name = {}
        
        