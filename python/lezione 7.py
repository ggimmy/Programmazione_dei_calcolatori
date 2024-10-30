#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:37:31 2024

@author: gimmyprog
"""

#Esercizio: def trova_posizione(a,v), restituire le posizioni di v in a
#NB!!! n appen() consecutivo costano O(n)

def trova_posizione(a, v):
    
    b = []
    
    i = 0
    for i in range(len(a)): #range(n) dove n è len(a)
        if a[i] == v:
            b.append(i)
        
        
        #COSTO FUNZIONE: O(n)
        
    return b

a = [1,2,3,2,3,4,5,6,2,3,4,5,6]

ris = trova_posizione(a, 2)
print(ris)

# In[Esercizio sottolineatura lezione 1 più efficente]
#L'esercizione della lezione 1 non era molto efficente, infatti la complessità
#temporale era di Theta(n**2)

a = 'pr0grammaz10ne de1 c4lc0lator1'
b = []

for x in a:
    if x in 'aeiouAEIOU': # O(1)
        b.append( '*' ) # O(1)
    elif x >= '0' and x <= '9': # O(1)'
        b.append( '#' ) # O(1)
    else:
        b.append( ' ' ) # O(1)
      
print(a)
print( ''.join(b) )   # O(n) 
#Il metodo .join, si applica sugli iterabili e concatena le stringhe separate
#da un carattere separatore esplicitato(in questo caso nessuno)

# In[Aliasing]

a = [1,2,3,2,3,4,5,6,2,3,4,5,6]

b = a # b in questo caso è solo un altro nome(alias) di a, entrambe le variabili
      # puntano allo stesso indirizzo di memoria
print(id(a), a)
print(id(b), b)

#per copiare una lista si utlizza lo slicing
c = a[:] #Copia a O(n)
print(id(c), c)

# In[Esercizio]

# def del_item(a, v):
#     '''
#     Input: a una lista; v un valore
#     Return: None
    
#     Elimina da a tutte le occorrenze di v
#     '''

def del_item(a, v):
    i = 0
    while i < len(a):
        if a[i] == v:
            del(a[i])
        else:
            i += 1
    #Costo computazionale funzione: O(n)
            
a = [4, 1, 7, 6, 5, 6, 8, 2, 3, 1, 2, 7, 8]
del_item(a, 1)
print(a)
