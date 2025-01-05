#include <stdio.h>
#include <stdlib.h>

/*
   Scrivere una funzione in C che, dati in input due array di interi a e b, ordinati in ordine non decrescente, crea una lista L contenente gli elementi nell'unione di a e di b.
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

lista esercizio(int *a, int*b);

int main(){

    int a[] = {2, 5, 6, 8, 8, 8, 8, 10, 12, 13};
    int b[] = {0, 0, 0, 1, 2, 3, 4, 5, 6, 13, 14};

    //lista L = init();

    lista L = esercizio(a,b);

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

lista esercizio(int *a, int*b){

    lista L = init();
    int i = 0;
    int j = 0;
    int n = 9;
    int m = 10;

    while(i < n){
        while(j < m){
            if(a[i] < b[j]){
                if(a[i] == a[i-1]){
                    i++;
                    continue;
                }
                L = append(L, intero(a[i]));
                i++;
            } else if(a[i] == b[j]){
                L = append(L, intero(b[j]));
                i++;
                j++;
            } else {
                if(b[j] == b[j-1]){
                    j++;
                    continue;
                }
                L = append(L, intero(b[j]));
                j++;
            }
        }
      
    }

    if(i <= n){
        while(i <= n){
            L = append(L, intero(a[i]));
            i++;
        }
    }

    if(j <= m){
        while(j <= m){
            L = append(L, intero(b[j]));
            j++;
        }
    }

    return L;


}

