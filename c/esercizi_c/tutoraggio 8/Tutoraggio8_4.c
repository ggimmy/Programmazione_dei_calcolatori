#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{

    int* a; //array
    int n;  //len

}array_int;

array_int esercizio(char* b, int n){
    array_int res = {NULL,0};
    
    int vocali = 0;
    for(int i = 0; i < n; i++){
        if(b[i] == 'a' || b[i] == 'e' || b[i] == 'i' || b[i] == 'o' || b[i] == 'u' || b[i] == 'A' || b[i] == 'E' || b[i] == 'I' || b[i] == 'O' || b[i] == 'U'){
            vocali++;
        }
    }

    res.a = malloc(sizeof(int)*vocali);
    int j = 0;

    for(int i = 0; i < n; i++){
        if(b[i] == 'a' || b[i] == 'e' || b[i] == 'i' || b[i] == 'o' || b[i] == 'u'|| b[i] == 'A' || b[i] == 'E' || b[i] == 'I' || b[i] == 'O' || b[i] == 'U'){
            res.a[j] = i;
            j++;
            res.n++;
        }
    }

    return res;


}

int main(){

    char s[] = "Algoritmi";
    int n = strlen(s); //len di b

    array_int res = esercizio(s,n);
    for(int i = 0; i < res.n; i++){
        printf("%d ", res.a[i]);
    }

    printf("\n");

}