# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:02:43 2020

@author: harshvardhan
"""
"""
Creating Database 
Creating Collections 
Inserting data into Collections
Checking DB exist or not 
Inserting one record

"""


from pymongo import MongoClient 

myClient = MongoClient('localhost',27017)
print(myClient.list_database_names())

myDB = myClient["Testing1"]
myCol = myDB["Testing_Collection"]


records = [
  { "id": 1, "name": "John", "address": "Highway 37"},
  { "id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "id": 3, "name": "Amy", "address": "Apple st 652"},
  { "id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "id": 5, "name": "Michael", "address": "Valley 345"},
  { "id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "id": 8, "name": "Richard", "address": "Sky st 331"},
  { "id": 9, "name": "Susan", "address": "One way 98"},
  { "id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "id": 12, "name": "William", "address": "Central st 954"},
  { "id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "id": 14, "name": "Viola", "address": "Sideway 1633"}
]
# This will insert all the records at once
myCol.insert_many(records)


# check if database exists or not
if "Testing1" in myClient.list_database_names():
    print("Yes")
else:
    print("Nope")