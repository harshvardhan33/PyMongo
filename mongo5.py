# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:02:38 2020

@author: harshvardhan
"""

"""
This code consistes of how i can delete the 
records in mongodb 


"""

from pymongo import MongoClient

myClient = MongoClient("localhost",27017)
myDB = myClient["Testing1"]
myCol = myDB["Testing_Collection"]

myQuery = {"name":"John"}
for i in myCol.find(myQuery):
    print(i)
 
print("After Delete")    
myCol.delete_one(myQuery)
for i in myCol.find(myQuery):
    print(i)