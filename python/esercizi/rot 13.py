#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del 
messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti 
nell'alfabeto.
Scrivere una funzione in grado di criptare una stringa in input, o decriptarla
se la stringa è già stata precedentemente codificata.
"""

def rot13(a):
    
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifrario   = "nopqrstuvwxyzabcdefghijklm"
    
    res = ""
    
    for c in a:
        if c == " ": #se c è uno spazio...
            res += " "
        else:
            i = 0
            while c != alfabeto[i]:
                i += 1
            
            res += cifrario[i]
            
    return res

def decode_rot13(a):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifrario   = "nopqrstuvwxyzabcdefghijklm"
    
    res = ""
    
    for c in a:
        if c == " ":
            res += " "
        else:
            i = 0
            while c != cifrario[i]:
                i += 1
                
            res += alfabeto[i]
            
    return res



a = 'ciao'
b = 'pvnb'
print(rot13(a))
print(decode_rot13(b))

        

    
#