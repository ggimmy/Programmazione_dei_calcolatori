#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:23:01 2024

@author: gimmyprog
"""
def permutazione(a,b):
   
    res = [0] * len(a)

    i = 0;

    while i <= 4:
        res[i] = a[ b[i] - 1]
        i += 1;
        
    return res

f = [3, 1, 4, 2, 5]
g = [5, 1, 3, 4, 2]

ris = permutazione(f, g)

print(ris)
