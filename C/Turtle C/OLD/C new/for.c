#include <stdio.h>

int main(){
    float saldo = 0;
    float salario;
    int cont;
    printf("Saldo: R$%.2f\n", saldo);
    printf("Digite seu salario mensal:\n--> ");
    scanf("%f", &salario);
    printf("Quantos meses restam ate terminar o contrato?\n--> ");
    scanf("%d", &cont);
    int i;
    for(i = 0; i != cont; i += 1){
        saldo += salario;
        printf("Mes %d: ", i+1);
        printf("R$%.2f\n", saldo);
    } 
    return 0;
}