#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:37:50 2017

@author: timothylenahan
"""

class companion():
    def __init__(self, com_name, com_condition, num_of_com):
        self.com_name = com_name
        self.com_condition = com_condition
        self.num_of_com = num_of_com
        
    def get_name(self):
        return self.com_name
    
    def set_name(self, com_name):
        self.com_name = com_name
        
    def get_condition(self):
        return self.com_condition
    
    def set_condition(self, com_condition):
        self.com_condition = com_condition
        
    def get_num_of_com(self):
        return self.num_of_com
    
    def set_num_of_com(self, num_of_com):
        self.num_of_com = num_of_com
        
    