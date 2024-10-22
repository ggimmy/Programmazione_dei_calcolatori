#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:32:38 2024

@author: gimmyprog

si scriva un programma che conti e stampi quante volte compare il carattere 
 (spazio) all'interno di una stringa legata alla variabile a. 
 Il programma deve far uso soltanto dei costrutti Python fin qua studiati. 
 Suggerimento: potrebbe essere utile un ciclo while che conta il numero di 
 spazi consecutivi a partire da una posizione e che sia 'annidato' nel ciclo
 principale che scorre i caratteri della stringa.
"""

testo = "pro gram ma zio ne"
a = 0
i = 0

while i < len(testo):
    
    while testo[i] == " ":
        a += 1
        i += 1
    
    i += 1

print(a)

# In[Esercizio 2]
"""
Modificare il codice precedente facendo in modo che il programma conti 
il numero di vocali minuscole all'interno della stringa. 
Risolvere il problema usando l'operatore 'in' di seguito descritto.
"""

testo = "ciao"
a = 0
i = 0
vocali = "aeiou"

while i < len(testo):
    if testo[i] in vocali:
        a += 1
    i += 1

print(a)
