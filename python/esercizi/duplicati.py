#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Input: [87, 45, 41, 65, 94, 41, 99, 94]

Lista modificata con duplicati rimossi: [87, 45, 41, 65, 99]

Si crea la tupla: (87, 45, 41, 65, 99)

Output: min: 41, max: 99
"""

def esercizio_lec3(a):
     
    a.sort()
    
    i = 0
    
    while i < len(a)-1:
            if a[i] == a[i+1]:
                del(a[i+1])
            else:
                    i += 1
            
    
    return a

a = [87, 45, 41, 65, 94, 41, 99, 94]
print(esercizio_lec3(a))
a = tuple(a)
print(a)
print('min: ',min(a), 'max: ', max(a))