# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 16:24:57 2022

@author: beyza
"""
from Person import Person

class Student(Person):
    def __init__(self,name,surname,gender,class_,number):
        self.class_ = class_
        self.number = number
        super().__init__(name, surname, gender)
    def display(self):
        print("Name : ",self.name)
        print("Surname : ",self.surname)
        print("Gender : ",self.gender)
        print("Class : ",self.class_)
        print("Number : ",self.number)
