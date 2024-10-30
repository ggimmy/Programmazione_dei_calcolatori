#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def perfetto(x):
    i = 1
    res = 0
    
    while i < x:
      
        if x % i == 0:
            res += i
            
        
        i += 1
    
    if res == x:
        return True
    else:
        return False
    
x = 28
print(perfetto(x))
            