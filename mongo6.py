# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:19:03 2020

@author: harshvardhan
"""

"""

Update the records
"""

from pymongo import MongoClient

myClient = MongoClient("localhost",27017)
myDB = myClient["Testing1"]
myCol = myDB["Testing_Collection"]


for x in myCol.find():
    print(x)