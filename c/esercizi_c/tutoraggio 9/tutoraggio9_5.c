#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
    Scrivere una funzione in C che, dati in input una lista L e una stringa s, modifica la lista L nel modo seguente: per ogni stringa s' contenuta in L, 
    la funzione deve concatenare le due stringhe s e s'. In particolare, se s' precede o è uguale a s, allora la concatenazione deve avere prima la stringa s' e poi s; viceversa,
    se s precede s', allora la concatenazione deve avere prima la stringa s e poi s'. La funzione deve ritornare il numero di elementi modificati nella lista L.
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

lista esercizio_v2(lista, char*);
int string_check(void*);

int main(){

    lista L = init();

    char s[] = "linguaggio";

    L = append(L, intero(2));
    L = append(L, fpoint(3.14));
    L = append(L, stringa("python"));
    L = append(L, intero(77));
    L = append(L, stringa("C"));
    L = append(L, stringa("java"));
    L = append(L, intero(23));
   
    L = esercizio_v2(L, s);
    
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


lista esercizio_v2(lista L, char* s){

    int n = strlen(s);
    int mod = 0;


    for(int i = 0; i <= L.n; i++){

        if(L.a[i].tipo == 's'){
           
            char* tmp = (char*)(L.a[i].dato);
            int m = strlen(tmp);

            if(strcmp(s,tmp) <= 0){
                char* new = malloc(sizeof(char)*(n+m+1));
                new = strcpy(new,s);
                new = strcat(new,tmp);
                mod++;
                L.a[i].dato = new;
            }   
           
            else{
                char* new = malloc(sizeof(char)*(n+m+1));
                new = strcpy(new, tmp);
                new = strcat(new, s);
                mod++;
                L.a[i].dato = new;
            }
        }
    }

    printf("Elementi modificati: %d\n",mod);
    return L;

}