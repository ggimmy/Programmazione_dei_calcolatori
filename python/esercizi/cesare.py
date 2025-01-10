#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:25:31 2024

@author: gimmyprog
"""

#Rifare con lambda

def cesare(a,k):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    def pos(a,c):
        j = 0
        while j < len(a):
            if a[j] == c:
                return j
            else:
                j+=1
            
            
            
    
    i = 0
    res = ""
    
    while i < len(a):
       
        if a[i] == " ":
            res += " "
            i += 1
        
        if a[i] in alfabeto:
            car = pos(alfabeto, a[i])
            index = (car + k) % 26
            res += alfabeto[index]
            i += 1
        
        
        
    return res

def dec_cesare(a,k):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    def pos(a,c):
        j = 0
        while j < len(a):
            if a[j] == c:
                return j
            else:
                j+=1
    
    i = 0
    res = ""
    
    while i < len(a):
       
        if a[i] == " ":
            res += " "
            i += 1
        
        if a[i] in alfabeto:
            car = pos(alfabeto, a[i])
            index = (car - k) % 26
            res += alfabeto[index]
            i += 1
    
    return res
    

a = "zaino"
b = "efnst"
print(cesare(a,5))
print(dec_cesare(b, 5))

# In[]

def pos(a,c):
       j = 0
       ret = 0
       while j < len(a):
           if a[j] == c:
               return j
           else:
               j+=1

a = "ciao"
print(pos(a,'a'))

# In[]

def cesare(a,k):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    def pos(a,c):
        j = 0
        while j < len(a):
            if a[j] == c:
                return j
            else:
                j+=1
      
    p = (lambda )
            
            
    
    i = 0
    res = ""
    
    while i < len(a):
       
        if a[i] == " ":
            res += " "
            i += 1
        
        if a[i] in alfabeto:
            car = pos(alfabeto, a[i])
            res += alfabeto[car+k]
            i += 1
        
        
        
    return res

def dec_cesare(a,k):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    def pos(a,c):
        j = 0
        while j < len(a):
            if a[j] == c:
                return j
            else:
                j+=1
    
    i = 0
    res = ""
    
    while i < len(a):
       
        if a[i] == " ":
            res += " "
            i += 1
        
        if a[i] in alfabeto:
            car = pos(alfabeto, a[i])
            res += alfabeto[car-k]
            i += 1
    
    return res
    

a = "zaino"
b = "kwfshjxht"
print(cesare(a,5))
print(dec_cesare(b, 5))
