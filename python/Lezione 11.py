#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clonazione profonda e deep copy utilizzando la ricorsione
@author: gimmyprog
"""

a = [ 'python', [0, 3.14, '2.71'], 100, ['programmazione', 'python'] ]
b = []

for x in a:
    if type(x) == list:
        b.append(x[:])
    else:
        b.append(x)
    
a[1][0] = 'uno'  #essendo b un clone di a, queste modifiche non avranno effetto
                 #su b
a[0] = 2014

print(b)

# In[]

def deep_copy(a):
    
    b = []
    
    for e in a:
        if type(e) != list:
            b.append(e)
        else:
            b.append(deep_copy(e))
            
    return b

a = [ 'python', [0, 3.14, '2.71'], 100, ['programmazione', 'python'] ]

print(deep_copy(a))
            
    