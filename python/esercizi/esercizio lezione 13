#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:59:15 2024


Data una lista di numeri ordinati in modo non decrescente ed un numero k

 Trovare la posizione dell'occorrenza più a destra di k in a: nell'esempio
 l'algoritmo ritorna 5. Se k non è in a, ritorna -1

@author: gimmyprog
"""

def bin_src(a,k):
    lx,rx = 0, len(a)-1
    
    if k < a[0] or k > a[-1]:
        return -1
    
    while lx <= rx:
        cx = int((lx+rx)/2)
        if k == a[cx]:
            return cx
        elif k < a[cx]:
            rx = cx-1
        else:
            lx = cx+1
            

def esercizio(a,k):
    
    if k in a == False:
        return -1
    
    p = bin_src(a,k)
    
    while a[p] == k:
        p += 1
        
    return p-1

a = [1, 5, 5, 7, 7, 7, 9, 9, 10, 13, 13, 14, 17]


k = 7
print(bin_src(a,k))
print(esercizio(a, k))
