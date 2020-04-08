#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:17:33 2017

@author: timothylenahan
"""

class Trailblazer():
    def __init__(self, name, miles, money, oxen, food, ammo, mis, meds, wagon, condition, food_consumed):
        self.name = name
        self.miles = miles
        self.money = money
        self.oxen = oxen
        self.food = food
        self.ammo = ammo 
        self.mis = mis
        self.meds = meds
        self.wagon = wagon
        self.condition = condition
        self.food_consumed = food_consumed
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_miles(self):
        return self.miles
    
    def set_miles(self, miles):
        self.miles = miles
        
    def get_money(self):
        return self.money
        
    def set_money(self, money):
        self.money = money
        
    def get_oxen(self):
        return self.oxen
    
    def set_oxen(self, oxen):
        self.oxen = oxen
        
    def get_food(self):
        return self.food
    
    def set_food(self, food):
        self.food = food
        
    def get_ammo(self):
        return self.ammo
    
    def set_ammo(self, ammo):
        self.ammo = ammo
        
    def get_mis(self):
        return self.mis
    
    def set_mis(self, mis):
        self.mis = mis
        
    def get_meds(self):
        return self.meds
    
    def set_meds(self, meds):
        self.meds = meds
    
    def get_wagon(self):
        return self.wagon
    
    def set_wagon(self, wagon):
        self.wagon = wagon
        
    def get_condition(self):
        return self.get_condition
    
    def set_condition(self, condition):
        self.get_condition = condition
        
    def get_food_con(self):
        return self.food_consumed
    
    def set_food_con(self, food_consumed):
        self.food_consumed = food_consumed