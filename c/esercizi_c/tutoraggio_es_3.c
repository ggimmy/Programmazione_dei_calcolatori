#include <stdio.h>
#include <stdlib.h>

/*
Scrivere una funzione in C che, dato un array di lunghezza m interi e un intero n, crea un array di lunghezza m+n che contiene:
    -Nelle prime m posizioni, gli interi contenuti nell'array in input nello stesso ordine;
    -In ognuna delle m+1 <= i <= m + n posizioni successiva, la somma di tutti gli interi nelle posizioni precedenti ad i;
*/

int *esercizio(int*, int, int);
int *esercizio_v2(int*, int, int);
int arr_sum(int*,int);


int main(){

    int m = 5;
    int arr[5] = {2, 3, 4, 5, 1};

    //int x = arr_sum(arr,m);
    //printf("%d\n", x);

    int *new = esercizio(arr, 3, 5);

    //DEBUG
    /*int *new = esercizio(arr, 3, 5);
    for(int i = 0; i < m; i++){
        printf("%d\n", new[i]);
    }*/

}

int arr_sum(int* arr, int len){

    int res = 0;

    for(int i = 0; i < len; i++){
        res += arr[i];
    }

    return res;

}

int *esercizio(int* arr, int n, int m){

    int *new = malloc(sizeof(int) * (m+n) );

    for(int i = 0; i < m; i++){
        new[i] = arr[i];
    }

   
    int j = m;

    while(j < n+m){

        new[j] = arr_sum(new, j);
        j++;

    }

    for(int k = 0; k < n+m; k++){
        printf("%d\n", new[k]);
    }

    return new;

}

