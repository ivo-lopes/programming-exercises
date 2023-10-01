#include <stdio.h>
#include <stdlib.h>

void main() {
    int x;
    int *p;
    p = &x;
    x = 10;
    printf("Endereço de x: %d\n", &x);
    printf("Endereço para qual p aponta: %d\n", p);
    printf("Conteudo de x: %d\n", x);
    printf("Conteudo de *p: %d\n", *p);    
}