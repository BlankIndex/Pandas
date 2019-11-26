#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:09:07 2019

@author: root
"""

import pandas as panda
cars = panda.read_csv('cars.csv')
print(cars[0:5],cars[27:32])


