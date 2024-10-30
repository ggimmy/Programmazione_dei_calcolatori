#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:32:47 2024

@author: gimmyprog
"""

#Miglioramento funzione del_item
def del_item(a, v):
    
    b = []
    
    for x in a:
        if x != v:
            b.append(x)
            
    i = 0
    while i < len(b):
        a[i] = b[i]
        i += 1 #i è la posizione del primo elemento da eliminare da a
    
    while i < len(a):
        del(a[-1])
    
    
L = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
del_item(L, 1)
print(L)

# In[Confronto fra tuple]

print ( (1, 3, 1) < (1, 2, 2) )

# print ( ('A', 3, 1) < (1, 2, 2) ) # TypeError

print ( (1, 3, 0) < (1, 3, 1, 2) )

print ( (1, 3, 1) < (1, 3, 1, 2) ) # tupla prefissa

# In[Esercizio punti su retta]

#Presuppongo di avere una lista con dei punti ('A', 1). Voglio ottenere una 
#stringa sul terminale dove nelle posizioni nella lista otteniamo la lettera
#del unto, altirmenti un asterisco.
#NB!! non modiicare inout ne utilizzare memoia agguntiva.

def punti_retta(a):
    #1) trovare gli intervalli:
    def t1(e):
        #Questa è la funzione che andremmo a dare in pasto all'argomento key
        #della funzione min() e max(), cosi che possa confrontare l'elemento in
        #pos 1 delle tuple nelle liste.
        return e[1];
        
    lx = min(a, key=t1)[1] #[1] ossia le tuple all'interno
    rx = max(a, key=t1)[1] 
    
    #ATTENZIONE: le funzioni min() e max() utilizzano < per confrontare, quindi
    #fare attenzione al confronto fra tuple!!!!
    
    for p in range(lx-1, rx+2):
        c = '*'
        for e, v in a:
            if p == v:
                c = e
        print(c, end='')
    

a = [ ('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5) ]
punti_retta(a)

#COSTO: O(n*m) m>n costo almeno qudratico in n
#SPAZIO O(1)
