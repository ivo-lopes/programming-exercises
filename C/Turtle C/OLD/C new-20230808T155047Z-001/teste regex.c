#include <ncurses.h>
#include <regex.h>
#include <string.h>
#include <stdlib.h>

int main() {
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);

    char entrada[100];
    getstr(entrada);

    endwin();

    if (strcmp(entrada, "sair") == 0) {
        printf("Voltando ao menu...\n");
        return 0;
    }

    regex_t regex;
    regmatch_t match[3];

    if (regcomp(&regex, "^(\\S+)\\s+(\\d+)$", REG_EXTENDED) != 0) {
        fprintf(stderr, "Erro ao compilar a expressão regular.\n");
        return 1;
    }

    if (regexec(&regex, entrada, 3, match, 0) == 0) {
        char direcao[100];
        strncpy(direcao, entrada + match[1].rm_so, match[1].rm_eo - match[1].rm_so);
        direcao[match[1].rm_eo - match[1].rm_so] = '\0';

        int numeroPassos = atoi(entrada + match[2].rm_so);

        // Aqui você pode executar ações com 'direcao' e 'numeroPassos'
    } else {
        printf("Comando inválido.\n");
    }

    regfree(&regex);

    return 0;
}
