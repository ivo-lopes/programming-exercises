#include <stdio.h>
#include <regex.h>

int main() {
    regex_t regex;
    int reti;
    char email[100];

    // Compile a expressão regular para validar o endereço de e-mail
    reti = regcomp(&regex, "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}$", REG_EXTENDED);
    if (reti) {
        fprintf(stderr, "Não foi possível compilar a regex\n");
        return 1;
    }

    printf("Digite um endereço de e-mail: ");
    scanf("%s", email);

    // Teste se o endereço de e-mail corresponde à regex
    reti = regexec(&regex, email, 0, NULL, 0);
    if (!reti) {
        printf("Endereço de e-mail válido!\n");
    } else if (reti == REG_NOMATCH) {
        printf("Endereço de e-mail inválido.\n");
    } else {
        char msgbuf[100];
        regerror(reti, &regex, msgbuf, sizeof(msgbuf));
        fprintf(stderr, "Erro na execução da regex: %s\n", msgbuf);
        return 1;
    }

    // Libere a estrutura da regex
    regfree(&regex);

    return 0;
}
