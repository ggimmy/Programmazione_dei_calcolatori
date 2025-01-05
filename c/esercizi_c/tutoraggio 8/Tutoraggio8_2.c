#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Conviene prima ordinare la lista e poi tagliarla;

void rimuovi(char *b, int i){

    int n = strlen(b);

    for(int j = i; j < n; j++){
        b[j] = b[j + 1];
    }
    

}

void esercizio(char* a, int len){

    
  char grande = a[0]; 
  int i = 0;
  while (a[i] != '\0') {
    if (a[i] >= grande) {
      grande = a[i];
      i++;
    }
    if(a[i]<grande){
        rimuovi(a,i);
    }
    

}
}

int main(){

    char a[] = "ddabeceffgfh";
    esercizio(a, strlen(a));
    printf("%s\n", a);

}