#include <stdio.h>

struct produto {
    int codbarra;
    float preco;
};

int main() {
    struct produto x;
    printf("Digite o codigo de barras do produto:\n-->");
    scanf("%d", &x.codbarra);
    printf("Digite o preco do produto:\n-->");
    scanf("%f", &x.preco);
    
    printf("Os dados do produto sao:\n");
    printf("Codigo: %d\n", x.codbarra);
    printf("Preco: R$%.2f", x.preco);
}