#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ESEMPIO:Ho dei punti su una retta ed un valore k. Voglio trovare la posizione
(segmento) la quale k appartiene sulla retta.
Posso confrontare tutta la lista(ricerca lineare, forza bruta) e metterci n
operazioni, oppure utilizzare la ricerca binaria.
"""

def bin_search_intervallo_retta(a,k):
    lx,rx = 0, len(a)-1 #inizializzo gli intervalli
    
    if k < a[0]:
        return ('-inf', a[0]) #utilizzo le parentsi nel return per ritornare
                              #coppie
    
    if k > a[-1]:
        return (a[-1], '+inf')
    
    while lx <= rx:
        cx = int((lx+rx)/2)
        if k == a[cx]:
            return (a[cx], a[cx+1])
        elif k < a[cx]:
            rx = cx-1
        else:
            lx = cx+1
            
    if k < a[cx]:
        return (a[cx-1], a[cx])
    elif k > a[cx]:
        return (a[cx], a[cx+1])

a = [-2, 3, 9, 12, 13]
k = 4

print(bin_search_intervallo_retta(a, k))

# complessità spaziale: O(1)
# complessità temporale: O(log_2 n)