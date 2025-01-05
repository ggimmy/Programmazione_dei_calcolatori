#include <stdio.h>
#include <stdlib.h>

/*
   Scrivere una funzione in C che, data in input una lista L e un indice p, elimina l'elemento in posizione p di L. In output, restituisce L.
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

lista lista_del(lista, int);

int main(){

    lista L = init();

    L = append(L, intero(12));
    L = append(L, intero(3));
    L = append(L, intero(6));
    L = append(L, intero(7));
    L = append(L, intero(9));

    L = lista_del(L, 2);
    
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

lista lista_del(lista L, int p){

    for(int i = p; i <= L.n; i++){
        L.a[i] = L.a[i+1];
    }
    L.n--;
    

    return L;

}