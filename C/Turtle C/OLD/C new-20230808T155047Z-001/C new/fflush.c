#include <stdio.h>

int main() {
    
char palavra1[10];
char palavra2[10];

printf("Primeira palavra:\n-->");
scanf("%s", palavra1);

printf("Segunda palavra:\n-->");
scanf("%s", palavra2);



}

/*O fflush faz a limpeza do buffer do método de entrada escolhido, 
que no caso é o teclado. Em muitos casos o fluxo do programa
é interrompido devido ao esgotamento do buffer de memória 
referente ao teclado, para resolver esse problema, o fflush é
capaz de fazer a limpeza desse buffer, se tornando a maior 
boa prática no que diz respeito à entrada de dados via teclado
na linguagem C*/