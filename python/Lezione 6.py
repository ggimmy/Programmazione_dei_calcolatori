#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:14:48 2024

@author: gimmyprog
"""
a = 'programmazione'

#Le stringhe sono immutabili: a[0] = 'P' NON SI PUO FARE (TypeError)

a = 'P' + a[1:] #Funziona ma crea una nuova stringa (slicing)

print(a) 

# In[Tuple]

t = 10, 11, 12 #inizializzazione tuple, una tupla è una serie di elementi.
t = (0, 'stringa', (1,2,3), 3.14)

print(t, type(t))

#Operazione tuple:
print((len(t))) #Conoscere il numero di elementi
print(t[2]) #Indicizzabile
print(t[::-1]) #Slicing

for x in t: #iterabilità
    print(x)

# In[packaging and unpackaging]
t = ('a','b','c')

x,y,z = t #spacchettamento

a = ()
a = x, y, z #inpacchettamento

print(a)
print(t)
print(z)

a, b = 1, 2

c = (a, b)

a = 10 #Non modifica la variabile a all'interno della lista, perchè è 
       #un elemento a se
       
print(c)

# In[Liste]
#La lista è una strutture dati modificabile, simile alla tupla

# len, indicizzazione, slicing, iterazione, concatenazione,
# ripetizione, spacchettamento sono ammesse


a = [0, 'stringa', (1,2)]
a[0] = 169
del(a[2]) #cancella l'elemento in posizione 2


#Per inserire in utilizziamo il metodo .append:
#un metodo è una funzione, applicata ad una struttura dati.
#Si può inserire in testa(meno efficente), o in coda(.append)

a.append(200)
print(a)

a  = a.append(0) #Ritorna none, perchè la funzione append, non ha un valore di
                 #ritorno ma modifica soltanto la lista
print(a)

# In[Esercizio]

# creare una lista che contiene i nomi dei punti in a a distanza al 
# più r da (O, 0,0)

a = [ ('A', 2,7), ('B',3, -1), ('C', 0, 1), ('D', -2,-2) ]
r = 2.9

b = []

for nome, x, y in a: #spacchettamento
    if x**2+y**2 <= r**2:
        b.append(nome)

#Complesità temporale algoritmo: O(n)

print(b)