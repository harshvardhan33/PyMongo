# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:33:49 2020

@author: harshvardhan
"""

import pymongo

# Create a mongodb Client to talk 
client = pymongo.MongoClient('localhost',27017)
mydb = client["Testing"]
information = mydb.tutorial2

record = [{'firstnmae':'Harsh1','lastname':'vd','Dept':'D1','qualification':'BE'},{'firstnmae':'Harsh2','lastname':'vd','Dept':'D2','qualification':'BE1'},{'firstname':'Harsh2','lastname':'vd1','Dept':'D3'},{'firstnmae':'Harsh3','lastname':'vd3','Dept':'D2'}]

information.insert_many(record)

#querying the database 
#print all the info
for i in information.find({}):
    print(i)
#only print for a condition
for i in information.find({'firstnmae':'Harsh1'}):
    print(i)
    


# wrting nested queries 
    