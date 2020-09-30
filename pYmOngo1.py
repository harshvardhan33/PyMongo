# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:42:12 2020

@author: harshvardhan
"""
import pymongo

# Create a mongodb Client to talk 
client = pymongo.MongoClient('localhost',27017)
mydb = client["DemoDB"]


information = mydb.testinginformation

record = [{'firstnmae':'Harsh1','lastname':'vd','Dept':'D1'},{'firstnmae':'Harsh1','lastname':'vd','Dept':'D1'},{'firstname':'Harsh2','lastname':'vd1','Dept':'D2'},{'firstnmae':'Harsh2','lastname':'vd3','Dept':'D2'}]


information.insert_many(record)

print(client.list_database_names())
