#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 17:34:46 2025

@author: gimmyprog
"""

import matplotlib.pyplot as plt

f = open('text.txt')

occ = {}

for line in f:
    for x in line:
        if x.isalpha():
            if x in occ:
                occ[x] += 1
            else:
                occ[x] = 1

#print(occ)

x = [ k for k in occ]
y = [ v for v in occ.values()]
    


print(x)
print(y)

plt.bar(x,y)
