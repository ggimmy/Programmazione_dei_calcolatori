#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:05:53 2024

@author: gimmyprog
"""

# In[Esercizio svolto in classe per gli 'if statements']
# Stampa a ed sottolineare con * le vocali e con # le
# cifre decimali
#
# Esempio
#
# pr0grammaz10ne de1 c4lc0lator1
#   #  *  * ## *  *#  #  # * * #

a = 'pr0grammaz10ne de1 c4lc0lator1'

b = ''

for x in a:
    if x in 'aeiou':
        b += '*'
    elif x >= '0' and x <= '9':
        b += '#'
    else:
        b += ' '

print(a)
print(b)

# In[Funzioni per ordine lessicografico]

#La funzione ord() stampa il valore dell carattere nella lista lesicografica
#La funzione chr() è l'inversa
print(ord('a')) 
print(ord('b'))
print('------------')
print(chr(97))
print(chr(98))
