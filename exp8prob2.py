#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:16:30 2019

@author: root
"""

import pandas as panda
cars = panda.read_csv('cars.csv')

#a
x=cars.iloc[1:10:2]
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

Mazda_Rx4=cars.loc[cars.loc[1,28,18,'Model'],["Model","cyl","gear"]];

print(Mazda_Rx4,ford,civic)

