# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:29:40 2020

@author: harshvardhan
"""

"""
Use of methods like 
find() : find all occurences
find_one() : find only one occurence
"""

from pymongo import MongoClient

myClient = MongoClient("localhost",27017)
myDB = myClient["Testing1"]
myCol = myDB["Testing_Collection"]

# Find all records
for x in myCol.find():
    print(x)

# Just one record
x = myCol.find_one({"name":"Hannah"})
print(x)