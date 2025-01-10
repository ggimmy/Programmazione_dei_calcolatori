#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
La congettura riguarda il seguente algoritmo:

    Si prende un intero positivo n ;
    Se n = 1 , l'algoritmo termina;
    Se n è pari, si divide per due; altrimenti si moltiplica per 3 e si aggiunge 1

La congettura di Collatz asserisce che questo algoritmo giunge sempre a termine, indipendentemente dal valore di partenza.

Scrivere una funzione che, dato un intero n in input, restituisce il numero di iterazioni necessarie affinché l'algoritmo termini, cioè dopo quante iterazioni risulta n = 1 .

Esempio: per n = 6 , allora abbiamo la successione

6 , 3 , 10 , 5 , 16 , 8 , 4 , 2 , 1 
"""

def collatz(n):
    
    if n == 1:
        return n
    
    if n % 2 == 0:
       n = n / 2
    else:
        n = (n*3) + 1
        
# In[]

def collatz(n):
    
    print(n)
    
    iterazioni = 1
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
            iterazioni += 1
        else:
            n = (n*3) + 1
            print(n)
            iterazioni += 1
    
    return iterazioni

            
collatz(6)
# In[]

def collatz(n):
    
    
    res = []
    res.append(n)
    iterazioni = 1
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            res.append(n)
            iterazioni += 1
        else:
            n = (n*3) + 1
            res.append(n)
            iterazioni += 1
    
    return (iterazioni, res)

            
collatz(6)