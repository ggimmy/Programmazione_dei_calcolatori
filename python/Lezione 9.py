#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:51:00 2024

@author: gimmyprog
"""

#MIGLIORAMENTO PUNTI SU RETTA(a scapito dello spazio)
#Il modo migliore per ottimizare la funzione è avere una lista già ordinata.
#Per utilizzarla utilizzeremo l'algoritmo di bubblesort, che porta in posizione
#n-1 il numero massimo ad ogni passata, ordinando la lista confrontando le coppie

def bubble_sort(a, key=None):
    def identity(e):
        return e  # Funzione identità in caso key resti None
    
    if key is None:
        key = identity
    
    n = len(a)
    
    for c in range(n-1):  # c è il numero di passate
        ordinata = True
        for i in range(n-1-c):  # sottraggo c per risparmiare passate
            if key(a[i]) > key(a[i+1]):  # se a[i] è maggiore di a[i+1]...
                a[i], a[i+1] = a[i+1], a[i]  # ...scambio
                ordinata = False  # se effettuo uno scambio, allora la lista non è ordinata
        if ordinata:
            break  # se la lista è ordinata, esco dalla passata corrente.


def punti_retta(a):
    def t1(e):
        return e[1]
    
    lx = min(a, key=t1)[1]
    rx = max(a, key=t1)[1]
    
    m = rx - lx + 1  # dimensione totale lista output
    retta = ['*'] * m  # tempo e spazio O(m)
    
    n = len(a)
    b = a[:]  # creo una copia così da non modificare l'input
    bubble_sort(b, key=t1)  # Ordina la copia b
    
    i = 0  # indice in b del prossimo punto da stampare
    
    for p in range(lx, rx + 1):
        if i < n and p == b[i][1]:  # Controlla se p è uguale al secondo elemento della tupla
            print(b[i][0], end=' ')  # Stampa il primo elemento della tupla (etichetta)
            i += 1
        else:
            print('*', end=' ')
    
    print()  # Per andare a capo dopo aver stampato tutto


# Test del codice
a = [('A', 6), ('B', -2), ('E', 3), ('C', 0), ('D', 5)]
punti_retta(a)