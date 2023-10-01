#include <stdio.h>

int main(){
    float saldo = 0;
    float salario;
    int cont = 0;
    printf("Saldo: R$%f\n", saldo);
    printf("Digite seu salario mensal:\n--> ");
    scanf("%f", &salario);
    while (cont < 12){
        saldo += salario;
        cont += 1;
        printf("Mes %d: ", cont);
        printf("R$%.2f\n", saldo);
    }
    printf("Saldo depois de 12 meses:\n--> R$%.2f", saldo);
    return 0;
}
