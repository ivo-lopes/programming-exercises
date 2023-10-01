#include <stdio.h>

int main(){
    int i;
    float preco[5] = {0,0,0,0,0};
    for (i = 0; i < 5; i++) {
        printf("Produto indice %d\nValor --> ", i);
        scanf("%f", &preco[i]);
    }
    for (i = 0; i < 5; i++) {
        printf("%.2f ", preco[i]);
    }

}