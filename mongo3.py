# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:53:21 2020

@author: harshvardhan
"""

"""
Custom Search Techiques in MongoDB
Find records using custom query

"""

from pymongo import MongoClient

myClient = MongoClient("localhost",27017)
myDB = myClient["Testing1"]
myCol = myDB["Testing_Collection"]

myQuery1 = {"name":"John"}
myQuery2 = {"name":"Hannah"}

count = 0
for i in myCol.find(myQuery1):
    print(i)
    count+=1
    
print(count)