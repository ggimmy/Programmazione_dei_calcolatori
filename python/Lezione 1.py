#variabili
x = 20
g = 5

while abs(g*g - x) > 0.00001: #mentre g*g non è abbastanza vicino a x
    print(g)
    g = (g+x/g)/2 #aggiorno g
                  #Utilizzando l'operatore '/' il valore di ritorno sarà un float
    
print("RIsultato", g) #stampa g una volta che la condizione sia soddisfatta
print(type(g))

# In[Radice quadrata migliorata, con input utente]

x = 20

g = input("inserisci numero di partenza ") 
    #La funzione input mette in attesa l'esecuzione del programma, 
    #aspettando un input dall'utente. La funzione input ritorna una 
    #stringa, per questo è poi necessario convertire la variabile nel
    #tipo di dato corretto, in questo caso float.
    #Se però nella sringa che vogliamo convertire, non è presente il
    #tipo di dato richiesto, otteniamo un ValueError
    # g = "ciao" g=float(g) ValueError

g = float(g)

while abs(g - x/g) > 0.00001:
    print(g)
    g = (g + x/g)/2
    
print("risultato: ", g)  

#se per sbaglio, cambio il nome a g, e mi dimentico di aggiornarlo nel resto 
#del programma, otterò un NameError  

# In[Contatore ed assegnamento multiplo]

x = 20

g, c = x/2, 0 #per ogni variabile (a,b) corrisponde un valore (x,y)

tentativi = 1000

#questo ciclo lo esegue in un massimo di 1000 tentativi, usando l'operatore
#logico and.
while abs(g - x/g) > 0.00001 and c < tentativi:
    c += 1 #incremento c di uno per verificare quante volte viene eseguito while
    g = g(g + x/g)/2