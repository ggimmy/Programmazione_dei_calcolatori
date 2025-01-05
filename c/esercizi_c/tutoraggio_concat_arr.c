#include <stdio.h>
#include <stdlib.h>

/*
    Scrivere una funzione in C che, dati due array a e b di int di lunghezza rispettivamente n e m, crea un'array che è la concatenazione di a e b, ossia,
     il nuovo array memorizza prima gli elementi di a e, a seguire, gli elementi di b.
*/

int *concatenazione(int* , int *, int , int );

int main(){

    int a[5] = {0,1,2,3,4};
    int b[3] = {5,6,7};
    int n = 5;
    int m = 3;

    int *res = concatenazione(a,b,n,m);

    for(int i = 0; i < (n+m); i++){
        printf("%d ",res[i]);
    }

     printf("\n");

}

int *concatenazione(int* arr_a, int *arr_b, int n, int m){

    int *res = malloc(sizeof(int)*(n + m));

    for(int i = 0; i < n; i++){

        res[i] = arr_a[i];

    }

    for(int i = 0; i < m; i++){
       
        res[i+n] = arr_b[i];
    
    }

    return res;

}