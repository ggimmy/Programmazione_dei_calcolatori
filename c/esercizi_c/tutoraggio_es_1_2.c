#include <stdio.h>

void scambio (int a, int b, int c){
    //Scrivere una funzione in C che, date tre varibili intere a, b e c, scambia gli interi contenuti in queste variabile in modo che a <= b <= c.

    printf("A = %d, B = %d, C = %d \n", a, b, c);
    
    if(a >= b){
        int tmp = a;
        a = b;
        b = tmp;
    } else if(a >= c){
        int tmp = a;
        a = c;
        c = tmp;
    }

    if(b >= c){
        int tmp = c;
        c = b;
        b = tmp;
    }

     printf("A = %d, B = %d, C = %d \n", a, b, c);

}

int *min_addr(int *arr, int n){

    //Scrivere una funzione in C che, dato un array di interi a e la sua dimensione n, restituisce l'indirizzo del più piccolo elemento contenuto in a.

    int *min = arr;

    for(int i = 0; i < n; i++){
        if(arr[i] <= arr[i+1]){
            min = &arr[i];
        }
    }

    return min;

}

int main(){
    printf("ES1: \n");
    scambio(5,7,2);

    printf("\nES2: ");
    int arr[5] = {21, 55, 5, 3, 53};
    int *min = min_addr(arr,5);
    printf("%p\n", &min);


    return 0;

}