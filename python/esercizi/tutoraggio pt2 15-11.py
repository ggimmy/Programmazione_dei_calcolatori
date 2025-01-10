#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:52:18 2024

@author: gimmyprog
"""

# In[]
'''
Scrivere una funzione pytthon che implementa l'algoritmo di ricerca binaria 
destra utilizzando la ricorsione

'''

#passare l'intervallo che va da cx a rx

def bin_ric(a, k, lx = 0, rx = None):
    
    if rx == None:
        rx = len(a)-1
    
    cx = int((lx+rx)/2)
    if a[cx] == k:
        return cx
    elif k < a[cx]:
        bin_ric(a,k,lx, cx-1)
    else:
        bin_ric(a, k, cx+1, rx)



a = [1,2,3,4,5,6,7,8,9]
print(bin_ric(a, 8))
# In[]
'''
Scrivere una funzione in python che date 2 liste ordinate di interi restituisce
una lista che è l'intersezione delle due liste.
Richiesta complessità temporale lineare nel totale delle len
'''

def intersezione(a,b):
    da, db = {}, {}
    
    for e in a:
        da[e] = None
    
    for e in b:
        db[e] = None
    
    c = []
    
    for e in da:
        if e in db:
            c.append(e)
    
    return c

a = [0, 1, 2, 4, 5, 6]
b = [1, 3, 4, 5, 6, 10]
#res=[1,4,5,6]

print(intersezione(a,b))

# In[]

def merge(a, b):
    '''
        Input: a una lista di elementi
            lx, cx e rx indici in a t.c. lx <= cx <= rx
            con la proprietà che a[lx:cx] e a[cx:rx] sono ordinate
        Output: None
        
        Effetto collaterale a[lx:rx] è ordinata
    '''

    i, j = 0,0
    c = []
    while i < len(a) and j < len(b):
      if a[i]!=b[j]:
          i += 1
      elif a[i] == b[j]:
          c.append(a[i])
          i += 1
          j += 1
   
    return c
        

a = [0, 1, 2, 4, 5, 6]
b = [1, 3, 4, 5, 6, 10]
#res=[1,4,5,6]

print(merge(a,b))

