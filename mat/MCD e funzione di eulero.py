#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:12:31 2024

@author: gimmyprog
"""

def mcd(a,b):
    #Algoritmo di eucleide
    if b == 0:
        return a
    
    if a % b == 0:
        return b
    
    while b > 0:
        r = a % b
        a = b
        b = r
        
        
    return a


def eulero(n):
    '''
    La funzione di eulero è definita come:
        Phi(n)=|{1<=i<=n : (n,i)=1}|
    Esempio:
        Phi(6)=|{1,5}|=2
    
    '''

    i = 1
    res = []
    
    while i <= n:
        if mcd(n, i) == 1: #O( n * 2log2(r))
            res.append(i)
        i += 1
    
    print(res) 
    return len(res)
  

    

a = 128
b = 200
n = 8
print(mcd(a,b))
print(eulero(n))