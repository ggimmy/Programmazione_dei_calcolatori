#include <stdio.h>
#include <stdlib.h>

struct nodo{

    int value;
    struct nodo *prev, *next;

};
typedef struct nodo nodo;

nodo* init(){
    return NULL;
}

void mostra_lista(nodo* a){

    nodo *i = a;

    while(i != NULL){
        printf("%d   ", i->value);
        i = i->next;
    }
    
    printf("\n");

}

nodo* in_0(nodo* a, int x){

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

int indSet(nodo* arr[], int* I, int n){

    for(int x = 0; x <= n-1; x++){

        if(I[x] == 1){

            while(arr[x] != NULL){

                if(I[arr[x]->value] == 1){
                    return 0;
                } else {
                    arr[x] = arr[x]->next;
                }
            
            }

        
        }
    
    }

    return 1;

}

int main(){

    int n = 4;

    nodo **arr = (nodo**)malloc(n*sizeof(nodo*)); //Inizializzazione di array di puntatori a nodo

    for(int i = 0; i < n; i++){
        arr[i] = init(); //Inizializzazione nodi
    }

    for(int i = 0; i < 9; i++){
        int r = rand() % (4 + 1 - 0) + 0;
        int r2 = rand() % (3+1-0) + 0;
        arr[r] = in_0(arr[r], r2);
    }
    
    for(int i = 0; i < n; i++){
            mostra_lista(arr[i]);
        }


    int I[4] = {0,1,0,0};

    int res = indSet(arr, I, n);

    printf("ARRAY BINARIO: ");

    for(int i = 0; i <= n-1; i++){
        printf("%d ", I[i]);
    }

    printf("\n");

    printf("INDSET: %d\n",res);

}