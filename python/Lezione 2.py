#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:03:16 2024

@author: gimmy
"""

x = "ciao"
y = "zero"
print(x > y) #False
             #Confronta le stringhe in ordine lessicografico

#La stringa prefisso contiene precede quella che la contiene
a = "ciao"
b = "ciaotutti"

print (a < b) #True

print(len(b)) #stampa la lunghezza di b, ossia il numero di caratteri della
              #stringa
              
#Concatenazione stringhe
c = "tutti"
print(a + " " + "a" + " " + c)

#ATTENZIONE! a + 2(int) = TypeError

print(a*4) #ripete la stringa per il numero di volte a destra

# In[Iterazione stringa]   

testo = "programmazione"           
i = 0

while i < len(testo):
    print(testo[i])
    i += 1
