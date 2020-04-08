#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:04:40 2017

@author: timothylenahan
"""

class Date():
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year
        
    def get_month(self):
        return self.month
    
    def set_month(self, month):
        self.month = month
        
    def get_day(self):
        return self.day
    
    def set_day(self, day):
        self.day = day
        
    def get_year(self):
        return self.year
    