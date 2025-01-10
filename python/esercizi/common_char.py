#!/usr/bin/env python3
"""
Scrivere un programma che date due stringe in input,
in output stampa solo i caratteri che la prima stringa
ha in comune con la seconda stringa.
"""
def common_char(a, b):
    res = "" #inizializzo stringa vuota che riempirò con concatenazioni
    i = 0
    n = 0
    
    if len(a) < len(b):
        n = len(a)
    else:
        n = len(b)
    
    while i < n:
        if a[i] == b[i] and a[i] not in res:
            res += a[i]
        
        i += 1
            
    return res

a = "ppogrammazione"
b = "prograsieossspasneosnas"

print(common_char(a, b))

# In[Miglioria]
def common_char(string, filtro):

    res = ""
    
    for c in string:
        if c in filtro:
            res += c
    
    return res

a = "ppogrammazione"
b = "prograsieossspasneosnas"

print(common_char(a, b))