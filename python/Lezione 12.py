#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:17:39 2024

@author: gimmyprog
"""
# In[Merge]

def merge(a,b):
    
    i = 0
    j = 0
    
    res = []
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    
    while i < len(a):
        res.append(a[i])
        i += 1
    
    while j < len(b):
        res.append(b[j])
        j += 1
    
    return res

a = [1,3,5,9,13]
b = [2,6,8,10,14,15]

print(merge(a,b))

# In[mergesort]

def merge(a, lx, cx, rx):
    
    i = lx
    j = cx
    
    res = []
    
    while i < cx and j < rx:
        if a[i] <= a[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(a[j])
            j += 1
    
    #Avanzi...
    while i < cx:
        res.append(a[i])
        i += 1
    
    while j < rx:
        res.append(a[j])
        j += 1
        
    i = lx
    for e in res:
        a[i] = e
        i += 1
    
    return a

def merge_sort(a, lx = 0, rx = None):
    
    if rx == None:
        rx = len(a) #Non posso inizializzare nella dichiarazione di funzione la
                    #variabile rx con len(a), perchè a ancora non è caricata 
                    #nella funzione.
    
    if lx+1 >= rx:
        return None #In caso di lista vuota o di un solo elemento per uscire 
                    #dalla funzione
    
    cx = int((lx+rx)/2) #Divido in 2 la lista n volte fino a che non finisco le
                        #coppie
   
    #Divido in log2(n) pezzi la lista...
    merge_sort(a, lx, cx)
    merge_sort(a, cx, rx)
    
    #Ordino i pezzi e li fondo tra loro.
    merge(a, lx, cx, rx)

a = [10, 21, 30, 34, 34, 38, 11, 13, 16, 17, 19, 0, 0, 10, 10]
merge_sort(a)
print(a)

#COMPLESSITÀ TEMPORALE: O(nlog2(n))
#COMLESSITÀ SPAZIALE: O(n)

# In[mergesort con stringhe]
    
a = ['programmazione', 'dei', 'calcolatori', '2024/25']
merge_sort(a) #Funziona in ordine lessicografico.
print(a)

# In[lambda function]

v = (lambda x: x**2)(2) #In questo caso assegno a v il valore ritornato dalla
                        #funzione lambda

f = lambda x:x #In questo caso f è una funzione.

# In[mergesort con ordinamento personalizzato]

#Possiamo personalizzare il criterio di ordinamento di mergesort, aggiungendo 
#una funzione key. Per esempio potrebbe essere utili per ordinare una lista che 
#contine sia numeri che stringhe, visto che con una normale mergesort otterrei
#TypeError.

def merge_sort(a , key = lambda x : x, lx = 0, rx = None):
    #Key è già inizzializzata a funzione identità.
    
    if rx == None:
        rx = len(a)
    
    if lx >= rx - 1:
        return a
    
    def merge(a, lx, cx, rx):
        
        #Definisco merge localmente in merge_sort visto che mi servirà 
        #solo per questa funzione
        
        
        i = lx
        j = cx
        
        res = []
        
        while i < cx and j < rx:
            if key(a[i]) <= key(a[j]):
                res.append(a[i])
                i += 1
            else:
                res.append(a[j])
                j += 1
        
        #Avanzi...
        while i < cx:
            res.append(a[i])
            i += 1
        
        while j < rx:
            res.append(a[j])
            j += 1
            
        i = lx
        for e in res:
            a[i] = e
            i += 1
        
        return a

    cx = int((lx+rx) /2 )
      
    merge_sort(a, key, lx, cx)
    merge_sort(a, key, cx, rx)
    merge(a, lx, cx, rx)
      
#Voglio ottenere una lista dove i numeri vengano prima delle stringhe.
#Per confrontarli, posso 'enumerarli' con una funzione.

def f(x):
    if isinstance(x, (int, float)):
        return (0, x)
    elif isinstance(x, str):
        return (1, x)
    else:
        return (2, str(x))
    
a = [10.4, 3.14, 'programmazione', 0, 'dei', 'calcolatori', 8, '2024/25']

merge_sort(a, key = f)

print(a)
