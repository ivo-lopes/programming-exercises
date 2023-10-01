#include <stdio.h>

int main() {
    char letra;
    printf("Digite uma letra qualquer: \n--> ");
    scanf("%c", &letra);
    printf("Você digitou isso:\n--> %c\n", letra);

    int inteiro;
    printf("Digite um número inteiro: \n--> ");
    scanf("%d", &inteiro);
    printf("Você digitou isso:\n--> %d\n", inteiro);

    float flutuante;
    printf("Digite um número não inteiro qualquer: \n--> ");
    scanf("%f", &flutuante);
    printf("Você digitou isso:\n--> %.2f\n", flutuante);
    return 0;
}