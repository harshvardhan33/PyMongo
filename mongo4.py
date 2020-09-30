# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:01:52 2020

@author: harshvardhan
"""

"""
Sorting the records that we need to fetch
We can sort the names according to the 
particular attribute
for sorting into the asce

"""

from pymongo import MongoClient

myClient = MongoClient("localhost",27017)
myDB = myClient["Testing1"]
myCol = myDB["Testing_Collection"]
myDoc = myCol.find().sort("name",-1)

for i in myDoc:
    print(i)
