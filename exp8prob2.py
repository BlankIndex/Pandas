#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:16:30 2019

@author: root
"""

import pandas as panda
cars = panda.read_csv('cars.csv')

#a
x = cars.iloc[:5,[1,3,5,7,9,11]]
print(x,"\n")

#b
mazda=cars[cars.loc[:,'Model']=='Mazda RX4']
print(mazda,"\n")

"\n"
#c
cars.loc[[22],'cyl']
bumblebee = cars.loc[cars.loc[:,'Model']=='Camaro Z28',['Model','cyl']]
print(bumblebee,"\n")


#d
Mazda_Rx4=cars.loc[cars.Model=='Mazda RX4',["Model","cyl","gear"]];
ford=cars.loc[cars.Model=='Ford Pantera L',["Model","cyl","gear"]];
civic=cars.loc[cars.Model=='Honda Civic',["Model","cyl","gear"]];

print(Mazda_Rx4ford,civic)
print(ford)
print(civic)

