# -*- coding: utf-8 -*-
"""
Created on Sat May  6 03:18:25 2023

@author: arman
"""

import json

employee=[{
  "name" : "Alex",
  "age" :  "25",
  "address" : "Paris"
}, {
  "name" : "Emily",
  "age" :  "18",
  "address" : "Toulouse"
}, {
  "name" : "Thomas",
  "age" :  "22",
  "address" : "Lile"
}]

with open('data.json', 'w') as mon_fichier:
	json.dump(employee, mon_fichier)
    
with open('data.json') as mon_fichier:
    data = json.load(mon_fichier)

print(data)
    