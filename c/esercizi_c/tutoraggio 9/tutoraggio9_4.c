#include <stdio.h>
#include <stdlib.h>

/*
   Scrivere una funzione in C che, dati in input due array di interi a e b, ordinati in ordine non decrescente, crea una lista L contenente gli elementi nell'intersezione di a e di b.
*/

typedef struct{

    char tipo;
    void *dato;

}elemento;

typedef struct{

    elemento *a;
    int n;
    int c;

}lista;

lista init();
lista append(lista, elemento);
void mostra(lista);

elemento intero(int);
elemento fpoint(float);
elemento stringa(char*);

lista esercizio(int *, int *, int, int);

int main(){

 
    int a[] = {2, 5, 6, 8, 8, 8, 8, 10, 12, 13};
    int b[] = {0, 0, 0, 1, 2, 3, 4, 5, 6, 13, 14};
    int n = 10;
    int m = 11;

    lista L = esercizio(a,b,n,m);
    mostra(L);

}

lista init(){

    lista lista_nuova = {NULL, 0 ,0};
    
    return lista_nuova;

}

lista append(lista L, elemento e){
    if (L.n == L.c) {
        L.c = 2*(L.c+1); 
        L.a = realloc( L.a, L.c*sizeof(elemento) );
    }
    
    L.a[L.n] = e;
    L.n++;
    
    return L;
}

void mostra(lista L){
    int i;
    
    printf("==================================\n");
    
    for(i = 0; i < L.n; i++){
        switch  (L.a[i].tipo) {
            case 'i':
                printf("%d\n", *((int*)L.a[i].dato) );
                break;
            case 'f':
                printf("%f\n", *((float*)L.a[i].dato) );
                break;
            case 's':
                printf("%s\n", (char*)L.a[i].dato );
                break;
        }
    }
    
    printf("dimensione %d, capacita' %d\n", L.n, L.c);
}


elemento intero(int x){
    elemento e = {'i', NULL};
    e.dato = malloc(sizeof(int));
    *((int*)e.dato) = x;

    return e;
}

elemento fpoint(float f){
    elemento e = {'f', NULL};
    e.dato = malloc(sizeof(float));
    *((float*)e.dato) = f;

    return e;
}

elemento stringa(char* s){
    elemento e = {'s', NULL};
    e.dato = s; //s è gia un puntatore

    return e;
}

lista esercizio(int *a, int *b, int n, int m){

    lista L = init();

    int j;

    for(int i = 0; i < n; i++){
        j = 0;
        while(j < m){
            if(a[i] == b[j]){
                L = append(L, intero(a[i]));
                break;    
            }
            j++;
        }
    }

    return L;

}