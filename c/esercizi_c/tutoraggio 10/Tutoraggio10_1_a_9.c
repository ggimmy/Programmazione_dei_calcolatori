#include <stdio.h>
#include <stdlib.h>



struct nodo{

    float value;
    struct nodo *prev, *next;

};
typedef struct nodo nodo;

//Prototipi
void mostra_lista(nodo*);
nodo* init();
nodo* in_0(nodo*, float);
nodo* cerca(nodo*, float);
nodo* del_0(nodo*);
nodo* del(nodo*, float);
nodo *insert(nodo*, float, int);


//esercizio
int lenLista(nodo*);
nodo *cercaPerPos(nodo*, int);

nodo *raddoppia(nodo*);
nodo *listaMediano(nodo*);
nodo *listaScambiaNodiCons(nodo*, nodo*);
nodo *estraiSegmento(nodo* , float, float);
nodo *cancellaTutto(nodo*, float);
nodo *invertiLista(nodo*);
nodo *listaInput(nodo*);
void arrayListeSort(nodo**, int);


int main(){

   nodo *a = init();

    a = in_0(a, 3.14);
    a = in_0(a, 2.71);
    a = in_0(a, 5.11);
    a = in_0(a, 4.67);
    a = in_0(a, 5.11);
    a = in_0(a, 5.21);


    //mostra_lista(a);

    //a = raddoppia(a);

    //nodo* i = listaMediano(a);

    //a = listaScambiaNodiCons(a,i);

    //nodo* a1 = estraiSegmento(a,5.11, 2.71);

    //a = cancellaTutto(a, 5.11);

    //a = invertiLista(a);
    
    //a = listaInput(a);

    //mostra_lista(a);


/*****************************************************************************************************************************************************/


    /*
    
    ESERCIZIO ARRAY DI LISTE ORDINATO
    
    */

    int n = 5;

    nodo **arr = (nodo**)malloc(n*sizeof(nodo*)); //Inizializzazione di array di puntatori a nodo

    for(int i = 0; i < n; i++){
        arr[i] = init(); //Inizializzazione nodi
    }

    //Riempimento randomico delle liste (per comodità esercizio)
    for(int i = 0; i < 20; i++){
        int r = rand() % (4 + 1 - 0) + 0;
        arr[r] = in_0(arr[r], 1.11);
    }
    
    //Prima
    for(int i = 0; i < n; i++){
        mostra_lista(arr[i]);
    }

    printf("SORTED-----------------------------\n");

    arrayListeSort(arr,n); //Implementata con uno scarso bubblesort

    //Dopo
    for(int i = 0; i < n; i++){
        mostra_lista(arr[i]);
    }

 

}

void mostra_lista(nodo* a){

    nodo *i = a;

    while(i != NULL){
        printf("%.2f   ", i->value);
        i = i->next;
    }
    
    printf("\n");

}

nodo* init(){

    return NULL;

}

nodo* in_0(nodo* a, float x){

    nodo *new = malloc(sizeof(nodo));
    new->value = x;
    new->next = a;
    new->prev = NULL;

    if(a != NULL){
        a->prev = new;
    }

    a = new;

    return a;

}

nodo* cerca(nodo* a, float x){

    nodo *i = a;

    while(i != NULL && i->value != x){
        i = i->next;
    }

    return i;

}

nodo* del_0(nodo* a){

    nodo *i = a;
    
    if(i == NULL){
        return i;
    }

    a = i->next;
    a->prev = NULL;
    free(i);

    return a;

}

nodo* del(nodo* a, float x){

    nodo *i = cerca(a,x);
    if(i == NULL){
        return a;
    }

    nodo *j = i->prev;
    if(j == NULL){
        return del_0(a);
    }

    j->next = del_0(j->next);
    if (j->next != NULL)
        j->next->prev = j;
    
    
    return a;

}

nodo *insert(nodo* a, float x, int pos){

    nodo *i = a;

    if(pos < 0)
        return a;
    

    if(pos == 0 || i == NULL)
        return in_0(a,x);
    
    while(pos != 1 && i->next != NULL){
        i = i->next;
        pos--;
    }

    nodo *j = in_0(i->next,x);
    i->next = j;
    j->prev = i;

    return a;
}

//esercizi

int lenLista(nodo* a){
    nodo *i = a;
    int numero_nodi = 0;
    while(i != NULL){
        numero_nodi++;
        i = i->next;
    }

    return numero_nodi;
}

nodo* raddoppia(nodo *a){
    //Scrivere una funzione in C che riceve in input una lista concatenata a con n nodi contenenti float ed aggiunge in fondo a questa n+1 nodi con valore 0.

    //calcolo i nodi della lista
    int n = lenLista(a);

    //definisco il range
    int j = 0;
    int range = (n*2);

    //aggiungo
    while(n != range){
        a = insert(a,0.0,n);
        n++;
    }

    return a;

}

nodo *listaMediano(nodo* a){

    int n = lenLista(a);

    nodo *i = a;
    
    int j = 0;
    while(j != (n/2) && i != NULL){
        i = i->next;
        j++;
    }

    return i;

}

nodo *listaScambiaNodiCons(nodo* a, nodo* b){

    float tmp = b->next->value;
    b->next->value = b->value;
    b->value = tmp;

    return a;

}

nodo *estraiSegmento(nodo* a , float v1, float v2){

    //cerco i nodi
    nodo *b = cerca(a, v1);
    nodo *c = cerca(a, v2);


    //se non trovati restituisco lista originale
    if(b == NULL && c == NULL){
        return a;
    }

    //inizializzo nuovo nodo
    nodo *a1 = init();

    //nodo iteratore
    nodo *i = b;

    //posizione degli elementi da inserire
    int pos = 0;
    
    //creazione segmento
    while(i->value != c->value){
        a1 = insert(a1, i->value, pos);
        pos++;
        i = i->next;
    }

    //ultimo elemento rimasto
    a1 = insert(a1, c->value, pos);

    return a1;

   
}

nodo *cancellaTutto(nodo* a, float x){

    
    //ciclo infinito, affinchè i non sia NULL(ovvero, quando non ci snono piu x nella lista)
    while(1){
    
    nodo *i = cerca(a,x);

    if(i == NULL){
        return a;
    }

    nodo *j = i->prev;
    if(j == NULL){
        a = del_0(a);
    }

    j->next = del_0(j->next);
    if (j->next != NULL)
        j->next->prev = j;
    
    
    }
    
    return a;

}

nodo* cercaPerPos(nodo*a, int pos){

    //se lista vuota o contiene 1 elemento...
    if(pos == 0 || pos < 0){
        return a;
    }
    
    //se posizione > len
    if(pos > lenLista(a)){
        printf("Not found\n");
        return a;
    }

    nodo *i = a;
    int c = 0;

    //cerco
    while(i != NULL && c != pos){
        c++;
        i = i->next;
    }

    return i;

}

nodo *invertiLista(nodo* a){

    int n = lenLista(a)-1;

    //se lista vuota o contiene 1elemento...
    if(n == 0 || n == 1){
        return a;
    }

    nodo *r = init();
    nodo *i = a;
    int rpos = 0;

    //creo nuova lista invertita
    while(i != NULL && n >= 0){
        i = cercaPerPos(a,n);
        r = insert(r, i->value, rpos);
        rpos++;
        n--;
    }

    //modifico a
    a = r;

    return a;

}

nodo *listaInput(nodo* a){

    while(1){

        //input inizializzato a zero così che ad ogni ciclo pulisce lo stream
        int input = 0;
        
        printf("Inserire intero: ");

        //la scanf ritorna 1 se il valore inserito è = al simbolo di formattazione
        int status = scanf("%d", &input);

        //se è stato inserito un intero lo aggiungo, altrimenti esco
        if(status == 1){
            a = in_0(a,input);
            mostra_lista(a);
        } else {
            printf("invalid char\n");
            return a;
        }

    }

    return a;

}

void arrayListeSort(nodo* arr[], int n){

    //Bubblesort molto semplice e poco efficiente (per l'esercizio)
    while(1){
        int pass = 0;
        for(int i = 0; i < n-1; i++){
            if(arr[i+1] != NULL && lenLista(arr[i]) > lenLista(arr[i+1])  ){
                nodo *tmp = arr[i+1];
                arr[i+1] = arr[i];
                arr[i] = tmp;
                pass++;
            }
        }

        if(pass == 0)
            return;

    }

    return;

}
