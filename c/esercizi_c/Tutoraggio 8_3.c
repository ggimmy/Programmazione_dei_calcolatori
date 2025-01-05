#include <stdio.h>
#include <stdlib.h>

typedef struct{

    int* a; //array
    int n;  //len

}array_int;

array_int esercizio(int* b, int n, int t){
    array_int res = {NULL,0};
    
    int counter = 0;
    for(int i = 0; i < n; i++){
        if(b[i] < t){
            counter++;
        }
    }

    res.a = malloc(sizeof(int)*counter);
    
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (b[i] < t) {
            res.a[j] = i;
            j++;
        }
    }
    
  
    res.n = counter;

    return res;


}

int main(){

    int b[] = {2,5,3,1,5,6,4,3,10,2};
    int n = 10; //len di b
    int t = 5; //soglia

    array_int res = esercizio(b,n,t);
    for(int i = 0; i < res.n; i++){
        printf("%d ", res.a[i]);
    }

    printf("\n");

}