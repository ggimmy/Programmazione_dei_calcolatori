#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char *prefix(char *, int );

int main(){

    char* a = "porcoddio";
    int n = 3;
    char* result = prefix(a,n);
    printf("%s\n",result);

}

char *prefix(char *a, int n){
    int m = strlen(a); //O(n)

    if(n < 0){
        printf("Inserire intero positivo\n");
        exit(0);
    } //O(1)

    if(n > m){
        char* risultato = malloc(sizeof(a)); //O(1)
        risultato = strcpy(risultato, a); //O(n)
        return risultato;
    }

    char* new = malloc(sizeof(char)*n);
    for(int i = 0; i < n; i++){ //O(n)
        new[i] = a[i]; //O(1)
    }

    return new;

    //Costo totale O(n)

}
