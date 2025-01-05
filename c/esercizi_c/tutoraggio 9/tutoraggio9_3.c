#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
    Scrivere una funzione in C che, date in input due stringhe a e b, 
    rimuove b da a nel caso in cui b sia sottostringa di a. La funzione deve restituire 0 se b non è sottostringa di a, 1 altrimenti.
 */

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

int esercizio(char *a, char *b){
    int n = strlen(a);
    int m = strlen(b);  
    int substr;
    
    for(int i = 0; i <= n - m; i++){
        substr = 1;
        for(int j = 0; j < m; j++){
            if(a[i + j] != b[j]){
                substr = 0;
                break;
            }
        }
        
        if(substr == 1){
           for(int j = i; j < n; j++){
            a[j] = a[j+m];
           }   
           printf("%s\n",a);
           return 1;
        }
    }


    return 0;  
}

int main(){

    char a[] = "programmazione dei calcolatori"; 
    char b[] = "azione";

    int res = esercizio(a,b);

    printf("%d\n",res);

}

int main0(){

    char *a = "Programmazione dei calcolatori";
    int n = strlen(a);
    int i = 4;
    int j = 18;

    char *p = sottostringa(a,n,i,j);
    printf("%s\n",p);

}