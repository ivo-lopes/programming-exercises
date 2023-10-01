#include <stdio.h>
#include <string.h>
#include <ncurses.h>
#include "funcoesMenu.h"

size_t metadetamanhostring(const char *str)
{
    size_t tamanho = strlen(str);
    return tamanho / 2;
}

void ciMenu(WINDOW *win)
{
    wclear(win);
    curs_set(false);
    noecho();
    cbreak();
}

void escreveinstru(WINDOW *win, int alturay, int largurax)
{

    char texto[17][100];
    strcpy(texto[0], "PRIMEIRO COLOQUE A DIRECAO E DEPOIS A DISTANCIA");
    strcpy(texto[1], "EXEMPLO: 'N 20'");
    strcpy(texto[2], "DIGITE 'modo 1' E 'modo 2' PARA TROCAR O MODO");
    strcpy(texto[3], "modo 1 (@) - modo de desenho");
    strcpy(texto[4], "modo 2 (#) - modo de borracha");
    strcpy(texto[5], "DIGITE 'sair' PARA VOLTAR PARA O MENU");
    strcpy(texto[6], "PARA APAGAR TODA A TELA DIGITE 'apagar'");
    strcpy(texto[7], "NORTE = n");
    strcpy(texto[8], "SUL = s");
    strcpy(texto[9], "LESTE = l");
    strcpy(texto[10], "OESTE = o");
    strcpy(texto[11], "NORDESTE = ne");
    strcpy(texto[12], "NOROESTE = no");
    strcpy(texto[13], "SUDESTE = se");
    strcpy(texto[14], "SUDOESTE = so");
    strcpy(texto[15], "TAMANHO DA MATRIZ EXIBIDO NA PARTE SUPERIOR");
    strcpy(texto[16], "ATUAL POSICAO EXIBIDA NA PARTE INFERIOR");

    wclear(win);
    box(win, 0, 0);
    mvwprintw(win, alturay / 18, ((largurax / 2) - metadetamanhostring(texto[0])), texto[0]);
    mvwprintw(win, (alturay / 18) * 2, (largurax / 2) - metadetamanhostring(texto[1]), texto[1]);
    mvwprintw(win, (alturay / 18) * 3, (largurax / 2) - metadetamanhostring(texto[2]), texto[2]);
    mvwprintw(win, (alturay / 18) * 4, (largurax / 2) - metadetamanhostring(texto[3]), texto[3]);
    mvwprintw(win, (alturay / 18) * 5, (largurax / 2) - metadetamanhostring(texto[4]), texto[4]);
    mvwprintw(win, (alturay / 18) * 6, (largurax / 2) - metadetamanhostring(texto[5]), texto[5]);
    mvwprintw(win, (alturay / 18) * 7, (largurax / 2) - metadetamanhostring(texto[6]), texto[6]);
    mvwprintw(win, (alturay / 18) * 8, (largurax / 2) - metadetamanhostring(texto[7]), texto[7]);
    mvwprintw(win, (alturay / 18) * 9, (largurax / 2) - metadetamanhostring(texto[8]), texto[8]);
    mvwprintw(win, (alturay / 18) * 10, (largurax / 2) - metadetamanhostring(texto[9]), texto[9]);
    mvwprintw(win, (alturay / 18) * 11, (largurax / 2) - metadetamanhostring(texto[10]), texto[10]);
    mvwprintw(win, (alturay / 18) * 12, (largurax / 2) - metadetamanhostring(texto[11]), texto[11]);
    mvwprintw(win, (alturay / 18) * 13, (largurax / 2) - metadetamanhostring(texto[12]), texto[12]);
    mvwprintw(win, (alturay / 18) * 14, (largurax / 2) - metadetamanhostring(texto[13]), texto[13]);
    mvwprintw(win, (alturay / 18) * 15, (largurax / 2) - metadetamanhostring(texto[14]), texto[14]);
    mvwprintw(win, (alturay / 18) * 16, (largurax / 2) - metadetamanhostring(texto[15]), texto[15]);
    mvwprintw(win, (alturay / 18) * 17, (largurax / 2) - metadetamanhostring(texto[16]), texto[16]);
    refresh();
}

void escrevecreditos(WINDOW *win, int alturay, int largurax)
{
    char texto[5][50];

    strcpy(texto[0], "LOGO TURTLE POR:");
    strcpy(texto[1], "PERI L. MACEDO");
    strcpy(texto[2], "BRUNO C. P. L. FILHO");
    strcpy(texto[3], "GUILHERME V. R. SILVA");
    strcpy(texto[4], "IVO L. S. NETO");

    wclear(win);
    box(win, 0, 0);

    mvwprintw(win, alturay / 8, (largurax / 2) - (metadetamanhostring(texto[0])), texto[0]);
    mvwprintw(win, (alturay / 8) * 2, (largurax / 2) - (metadetamanhostring(texto[1])), texto[1]);
    mvwprintw(win, (alturay / 8) * 3, (largurax / 2) - (metadetamanhostring(texto[2])), texto[2]);
    mvwprintw(win, (alturay / 8) * 4, (largurax / 2) - (metadetamanhostring(texto[3])), texto[3]);
    mvwprintw(win, (alturay / 8) * 5, (largurax / 2) - (metadetamanhostring(texto[4])), texto[4]);
    refresh();
}

void mainmenu(WINDOW *win, int alturay, int largurax)
{
    char texto[5][50];

    strcpy(texto[0], "LOGO TURTLE");
    strcpy(texto[1], "JOGAR");
    strcpy(texto[2], "INSTRUCOES");
    strcpy(texto[3], "CREDITOS");
    strcpy(texto[4], "SAIR");

    box(win, 0, 0);
    mvwprintw(win, alturay / 4, (largurax / 2) - (metadetamanhostring(texto[0])), texto[0]);
    mvwprintw(win, (alturay / 2) - 1, (largurax / 2) - metadetamanhostring(texto[1]) - 1, texto[1]);
    mvwprintw(win, alturay / 2, (largurax / 2) - (metadetamanhostring(texto[2])), texto[2]);
    mvwprintw(win, (alturay / 2) + 1, (largurax / 2) - (metadetamanhostring(texto[3])), texto[3]);
    mvwprintw(win, (alturay / 2) + 2, (largurax / 2) - (metadetamanhostring(texto[4])), texto[4]);
    wrefresh(win);
}

void menumov(WINDOW *win, int alturay, int largurax, int opcao)
{
    char seta[3];
    char texto[5][50];

    strcpy(texto[0], "LOGO TURTLE");
    strcpy(texto[1], "JOGAR");
    strcpy(texto[2], "INSTRUCOES");
    strcpy(texto[3], "CREDITOS");
    strcpy(texto[4], "SAIR");

    strcpy(seta, "->");

    if (opcao % 4 == 0)
    {

        mvwprintw(win, (alturay / 2) - 1, (largurax / 2) - metadetamanhostring(texto[1]) - 3, "%s", seta);
        mainmenu(win, alturay, largurax);
        wrefresh(win);
    }
    else if (opcao % 4 == 1)
    {

        mvwprintw(win, alturay / 2, (largurax / 2) - metadetamanhostring(texto[2]) - 2, "%s", seta);
        mainmenu(win, alturay, largurax);
        wrefresh(win);
    }
    else if (opcao % 4 == 2)
    {
        mvwprintw(win, (alturay / 2) + 1, (largurax / 2) - metadetamanhostring(texto[3]) - 2, "%s", seta);
        mainmenu(win, alturay, largurax);
        wrefresh(win);
    }
    else if (opcao % 4 == 3)
    {
        mvwprintw(win, (alturay / 2) + 2, (largurax / 2) - strlen(texto[4]), "%s", seta);
        mainmenu(win, alturay, largurax);
        wrefresh(win);
    }
}
