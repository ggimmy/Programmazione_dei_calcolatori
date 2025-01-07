#include <stdio.h>
#include <math.h>
#include <limits.h>

//colors
#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_MAGENTA "\x1b[35m"
#define ANSI_COLOR_CYAN    "\x1b[36m"
#define ANSI_COLOR_RESET   "\x1b[0m"


#define MAX_SIZE 1024/12
/*
----------------------MENU----------------------
-SEND
-DECRYPT
-ADD RECEIVER
-LIST
-QUIT

*/

typedef struct receiver{

    char name; //single char name
    int n;
    int e;

}receiver;

void menu(receiver*, int); //menu call
void print_menu();//menu selector;
int choice();
receiver* add_receiver(receiver*, int); // aggiunge un destinatario
void show_receivers(receiver*, int);
void encrypt(receiver*, int);
void decrypt();

int main(){


    receiver array[MAX_SIZE]; //inizializzazione array che conterrà i destinatari (MAX 1kb)
    int pos = 0; //index init

    menu(array,pos);

    return 0;
}

void print_menu(){

    printf(ANSI_COLOR_GREEN "\t\tSIMPLE RSA CODE DECRYPTER-ENCRYPTER\n\n" ANSI_COLOR_RESET);
    printf("1-SEND MESSAGE\n\n");
    printf("2-DERCYPT MESSAGE\n\n");
    printf("3-ADD RECEIVER\n\n");
    printf("4-LIST ALL\n\n");
    printf("5-QUIT\n\n");


}
int choice(){
    int ch = 0;
    scanf("%d",&ch);

    if(ch > 5){
        printf("ERROR > 5\n");
        return 5;
    }

    return ch;
}

receiver* add_receiver(receiver* arr, int pos){

    printf(ANSI_COLOR_BLUE "\t\tDIMENSIONE MAX 1KB: DESTINATARI RIMASTI: %d\n\n" ANSI_COLOR_RESET, MAX_SIZE-pos);

    char bin;
    scanf("%c",&bin);

    printf("Inserire nome destinatario: ");
    scanf("%c", &arr[pos].name);
    printf("inserire parametro n: ");
    scanf("%d", &arr[pos].n);
    printf("Inserire parametro e: ");
    scanf("%d", &arr[pos].e);
    return arr;

}

void show_receivers(receiver* arr, int pos){

    if(pos == 0){
        printf("EMPTY");
        return;
    }

    for(int i = 0; i < pos; i++){
        printf("INDEX NUMBER: %d",i);
        printf("NAME: %c\n", arr[i].name);
        printf("n = %d\n", arr[i].n);
        printf("e = %d\n\n", arr[i].e);
    }

}

void encrypt(receiver* arr, int pos){

    if(pos == 0){
        printf(ANSI_COLOR_YELLOW "\nNO RECEIVERS FOUND !!\n\n" ANSI_COLOR_YELLOW);
        return;
    }

    int ch = 0;
    printf("Scegli il destinatario (DIGITARE IL SUO INDEX NUMBER) ");
    scanf("%d", &ch);

    unsigned long long int m = 0;
    printf("Inserire messagio da criptare: ");
    scanf("%llu", &m);

    if((m = pow(m,arr[ch].e)) <= ULLONG_MAX){
        printf("\n\nMESSAGGIO CRIPTATO = %llu\n\n", m % arr[ch].n);
    } else {
        printf(ANSI_COLOR_RED "\nOVERFLOW!\n\n" ANSI_COLOR_RESET);
        return;
    }



    //printf("MESSAGGIO CRIPTATO = %llu", m % arr[ch].n);

}

void decrypt(){

   unsigned long long int m = 0;
    int d = 0;
    int n = 0;
    printf("Inserire messaggio da decifrare: ");
    scanf("%llu", &m);
    printf("Inserire parametro d: ");
    scanf("%d", &d);
    printf("Inserire vostro parametro n: ");
    scanf("%d", &n);

    m = pow(m,d);

    printf("\n\nMESSAGGIO DECIFRATO: %llu\n\n", m % n);

}

void menu(receiver* arr, int pos){

    int x = 1;

    while(x){
        print_menu();
        switch (choice()) {
            case 1:
            encrypt(arr, pos);
            break;
            case 2:
            decrypt();
            break;
            case 3:
            add_receiver(arr, pos);
            pos++;
            break;
            case 4:
            show_receivers(arr, pos);
            break;
            case 5:
            x = 0;
            break;
        }

    }

}
