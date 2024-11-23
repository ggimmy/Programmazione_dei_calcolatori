#include <stdio.h>

float potenza(float x, int e){
//Calcola la potenza di x,quindi ritorna x^e

    int i = 0;
    float result = 1;
    for(i = 0; i < e; i++){

        result *= x;

    }

    return result;

}

int main(){

    float x = 3;
    int e = 9;

    x = potenza(x, e);

    printf("%.2f\n", x);

    return 0;


}