#include <stdio.h>
#include <stdlib.h>

int fattoriale(int x){

    int fact = 1, i;

    for (i = 1; i <= x; i++) {
        fact *= i;
    }

    return fact;

};

int* arr_fact(int);

int main(){

    int n = 5;

    int *res = arr_fact(n);

    for(int i = 0; i <= n; i++){
        printf("%d ",res[i]);
    }

     printf("\n");


}

int *arr_fact(int n){

    int *res = malloc(sizeof(int)*n);

    for(int i = 0; i <= n; i++){
        res[i] = fattoriale(i);
    }

    return res;

}