#include <stdio.h>
#include <locale.h> 

int main() {

    setlocale(LC_ALL, "Portuguese");

    char frase[12];
    printf("Digite um texto:\n");
    fgets(frase, 12, stdin);
    printf("Texto digitado: %s\n", frase);
}

/*o gets recebe strings mas não delimita o tamanho do vetor,
portanto se a string inserida for maior do que a memória alocada
no vetor que armazena a string, isso vai dar erro. Para isso 
se utiliza o fgets que nada mais é do que um gets mas com o "f"
de formatado. o fgets é uma função que recebe não apenas o nome
da variável que armazena uma string, mas também o tamanho 
máximo alocado para esse vetor e o meio de entrada que por padrão 
é o "stdin" (entrada do teclado).*/