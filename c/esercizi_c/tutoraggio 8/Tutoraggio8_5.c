#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* concatenazione(char*a, char*b){

    int n = strlen(a);
    int m = strlen(b);

    char *p = malloc(sizeof(char)*(n+m));

    if(n < m){
        p = strcpy(p,a);
        p = strcat(p, b);
    }

    return p;

}

int main(){

    char *a = "prolog";
    char *b = "programmazione";

    char *p = concatenazione(a,b);
    printf("%s\n",p);
}