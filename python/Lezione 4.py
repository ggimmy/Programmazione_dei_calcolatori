#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:34:39 2024

@author: gimmyprog
"""
# In[Da maiuscolo a minuscolo]
c = 'D'
 
if c >= 'A' and c <='Z': #se c è maiuscolo...
    delta = ord(c) - ord('A') #Calcola la posizione della variabile c rispetto
                              #ad 'A', il primo dei maiuscoli
   
    c_min = chr(ord('a') + delta) #Aggiungendo ad 'a' il delta calcolato in
                                  #in precedenza, otterremo il risultato sperato
    
print(c_min)

# In[Funzioni]

"""
Def è la parola chiave per dichiarare una funzione, una funzione DEVE ritornare
qualcosa.
Le variabili all'interno di una funzione, sono dette variabili locali(ossia 
valgono solo nell'ambiente della funzione)
"""

def sqrt(x):
    g, c = x/2, 0 #variabili locali
    
    eps, c_max = 0.00000000001, 1000
    
    while abs( g - x/g ) >  eps and c < c_max:
        c = c+1
        g = ( g + x/g )/2

    return g #senza il risultato è None
    
ris = sqrt(20) #In questo caso assegnamo a ris il valore della funzione sqrt(20)
               #che a sua volta è dato dal valore di g al suo interno
               #Ad ogni chiamata di funzione, deve corrispondere il numero 
               #esatto di argomenti, sennò si otterrà un TypeError!
print(ris)

# In[Continuo funzioni]
"""
Posso anche non assegnare valori alle variabili locali nella funzione, per poi
assegnarli in fase di chiamata.
Oppure in fase di dichiarazione, posso assegnare dei valori di default agli
argomenti.
Se si specifica il nome delle variabile a cui stiamo assegnando un valore in 
fase di chiamata, ordine dei valori non cambia.
Esempio ordine valori: fun(a,b,c) prod.cart fun(1,2,3)
""" 
def sqrt( x, eps=0.01, c_max=100 ):
    g, c = x/2, 0 #variabili locali
    
    while abs( g - x/g ) >  eps and c < c_max:
        c = c+1
        g = ( g + x/g )/2

    return g #senza il risultato è None
    
print( sqrt(20, 0.00001, 10000) )
print( sqrt(20) )
print( sqrt(20, 0.1) )
print( sqrt(20, c_max=2) )
print( sqrt(c_max = 2, x = 20) )

# In[Problema: Palindromi]

"""
Verificare che la stringa sia un palindromo
"""

def palindromo(testo):
    i = 0;
    n = len(testo)

    while i < n/2 and testo[n-i-1] == testo[i]:
        return True

    return False


print(palindromo('012kayak210'))



# In[Slicing]

#NB!! Se indichiamo un indice neativo, python scorrerà la lista al contrario a
#partire dal carratere in pos n-1

a = '0123456789'

print(a[-2]) #Ritorna 8, il caratter appunto in pos - 2
print(a[1:7]) #Taglia la stringa dalla pos 1 alla 7(escluso)
print(a[:7]) #Omettendo uno dei due operandi, implico che voglio tagliare la
             #stringa a partire dall'inizio o dalla fine   
print(a[1:])
print(a[:]) #Ristampa un CLONE della lista
print(a[1:7:2]) # slicing con, ovvero taglia la stringa da 1 a 7-1 per poi far
                #rimanere solo i carattare in ogni n-1 posizioni
print(a[::-1]) #Inverte la stringa

#ATTENZIONE! OGNI VOLTA CHE SI USA LO SLICING, VIENE CREATA UNA NUOVA STRINGA!!

