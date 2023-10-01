#include <stdio.h>

int main(){
    int idade;
    printf("Insira sua idade: \n--> ");
    scanf("%d", &idade);
    printf("Idade informada: %d anos.\n", idade);
    if (idade <= 10) {
        printf("10 anos atras voce nao existia\n");
    } else {
        printf("10 anos atras voce tinha %d anos.", idade-10);
    }
    return 0;
}