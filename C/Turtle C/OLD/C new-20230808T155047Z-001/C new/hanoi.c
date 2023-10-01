#include <stdio.h>

// Função que realiza (imprime) o movimento
// de um disco entre dois pinos
void mover(int O, int D) {
    printf("%d -> %d\n", O, D);
}

// Função que implementa a recursão
// O = pino origem
// D = pino destino
// T = pino de trabalho
void hanoi(int n, int O, int D, int T) {
    if (n > 0) {
        hanoi(n - 1, O, T, D);
        mover(O, D);
        hanoi(n - 1, T, D, O);
    }
}

int main() {
    int n; // número de discos

    // Recebe o número de discos digitado pelo usuário
    printf("Digite o número de discos: ");
    scanf("%d", &n);

    // Executa o hanoi!
    hanoi(n, 1, 3, 2);

    return 0;
}
