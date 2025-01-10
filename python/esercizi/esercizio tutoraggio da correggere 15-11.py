#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:52:57 2024

@author: gimmyprog
"""

# In[]
'''

Scrivere una funzione in python che , data una lista binaria(0,1), ordina la 
lista a. La funzione deve avere complessità temporale in len(a), e complessità
spaziale costante

SOLUZIONE: Conto gli uno e gli zeri, e poi modifico la lista per quanti sono

'''

def ord_bin(a):
    
    n = len(a) #rispettare la complessità temporale in n
    
    for c in range(n-1):
        for i in range(n-1-c):
            if a[i]>a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    
    return(a)
    
    


a = [0,1,0,0,1,1,1,1,0,1,1]

print(ord_bin(a))

# In[]

def ord_bin(a):
    
    n = len(a) #rispettare la complessità temporale in n
    
    i = 0
    
    
    while i < len(a):
        if a[i] == 1:
            del(a[i])
            a.append(1)
            i += 1
        else:
            i+=1
            

    
    return(a)
    
    


a = [0,1,0,0,1,1,1,1,0,1,1]

print(ord_bin(a))

# In[]
def ord_bin(a):
    
    n = len(a) #rispettare la complessità temporale in n
    
    i = 0
    
    
    while i < len(a):
        if a[i] == 1:
            a[-1] == a[i]
            i += 1
        else:
            i+=1
            

    
    return(a)
    
    


a = [0,1,0,0,1,1,1,1,0,1,1]

print(ord_bin(a))