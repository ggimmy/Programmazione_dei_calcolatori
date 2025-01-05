#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* sottostringa(char*a, int n, int i, int j){
    
    if(j > n){
        j = n;
    }
    if(i < 0){
        i = 0;
    }

    char *p = malloc(sizeof(char)*(j - i));
    if(p == NULL){
        printf("ERROR! MALLOC() FAILED\n");
        exit(0);
    }

    int h = 0;
    for(int k = i; k <= j; k++){
        p[h] = a[k];
        h++;
    }

    return p;

}

int main(){

    char *a = "Programmazione dei calcolatori";
    int n = strlen(a);
    int i = 4;
    int j = 18;

    char *p = sottostringa(a,n,i,j);
    printf("%s\n",p);

}