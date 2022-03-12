# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 16:23:12 2022

@author: beyza
"""

class Person(object):
    def __init__(self,name,surname,gender):
        self.name = name
        self.surname = surname
        self.gender = gender
    def display(self):
        print("Name : ",self.name)
        print("Surname : ",self.surname)
        print("Gender : ",self.gender)