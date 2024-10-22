#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:01:31 2024

@author: gimmyprog
"""

#COSTO COMPUTAZIONALE: Quanto ci mette l'algoritmo ad essere eseguito?

def lettera(c):
    return c >= 'a' and c <= 'z' #Tempo costante(ossia operazioni che non 
                                 # crescono al variare dell'input)

def conta_parole(a):

    parole = 0
    p_flag = False
  #^^^^^^^^^^^^^^ costanti
    
    for c in a: #Tempo n, dove n sta per la len(a)
        if lettera(c):
            if not p_flag:
                parole += 1
                p_flag = True
        else:
            if p_flag:
                p_flag = False
      
    return parole
#^^^^^^^^^^^^^^^^^^^^^^ tutto il resto della funzione è in tempo costante.

#La complessità temporale, si calcola con le notazioni asintodiche quindi,
#andiamo a rimuovere le operazioni costanti(perchè n = +infinito quindi le
#costanti sono inutili) e rimaniamo solo con n. In questo caso la funzione
#è lineare in n scritto O(n)

a = " programmazione dei calcolatori "

print(conta_parole(a))
