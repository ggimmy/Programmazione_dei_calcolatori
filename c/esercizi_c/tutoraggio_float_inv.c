#include <stdio.h>
#include <stdlib.h>

/*
    Scrivere una funzione in C che, dato un'array a di float di lunghezza n, crea un'array che è l'inverso di a, ossia, il nuovo array memorizza gli elementi di a al contrario.
*/

float* rev_float(float *arr, int len);

int main(){

    int n = 5;
    float a[5] = {1.4, 2.3, 2.33, 5.66, 1};

    float *res = rev_float(a, n);

    for(int i = 0; i < n; i++){
        printf("%.2f ",res[i]);
    }
    printf("\n");

}

float* rev_float(float *arr, int len){

    float *res = malloc(sizeof(float)*len);

    int i = len-1;
    int j = 0;

    while(i >= 0 && j < len){
        res[j] = arr[i];
        j++;
        i--;
    }

    return res;

}
