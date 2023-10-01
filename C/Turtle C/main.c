#include <stdio.h>
#include <string.h>
#include <ncurses.h>
#include "funcoesMenu.h"
#include "funcoesJogo.h"

int main()
{

    initscr();      // inicializa o modo tela do ncurses
    ciMenu(stdscr); // configura a tela inicial

    int y, x, opcao, loop;
    getmaxyx(stdscr, y, x); // pega a informa��o do tamanho maximo y,x do console
    opcao = 0;
    loop = 1;

    WINDOW *win = newwin(y, x, 0, 0); // cria uma janela

    box(win, 0, 0); // escreve a borda da janela

    refresh();           // atualiza a tela principal (stdscr)
    wrefresh(win);       // atualiza a janela informada
    mainmenu(win, y, x); // fun��o que escreve o menu principal

    while (loop == 1) // loop onde a intera��o com o menu acontece
    {
        int key = wgetch(win);
        keypad(win, TRUE);
        menumov(win, y, x, opcao);
        if (key == KEY_UP)
        {
            opcao -= 1;
            if (opcao < 0)
                opcao = 3;

            clear();
            wclear(win);
            box(win, 0, 0);
            menumov(win, y, x, opcao);
        }
        else if (key == KEY_DOWN)
        {
            opcao += 1;
            clear();
            wclear(win);
            box(win, 0, 0);
            menumov(win, y, x, opcao);
        }
        else if (key == '\n')
        {
            if (opcao % 4 == 0) {
                //comando para JOGAR
                jogar();
                wgetch(win);
                wclear(win);
                mainmenu(win, y, x);
                menumov(win, y, x, opcao);
            }  
            else if (opcao % 4 == 1)
            {
                //comando para mostrar as INSTRUÇÕES
                escreveinstru(win, y, x);
                wgetch(win);
                wclear(win);
                mainmenu(win, y, x);
                menumov(win, y, x, opcao);
            }
            else if (opcao % 4 == 2)
            {
                //comando para mostrar os CRÉDITOS
                escrevecreditos(win, y, x);
                wgetch(win);
                wclear(win);
                mainmenu(win, y, x);
                menumov(win, y, x, opcao);
            }
            else if (opcao % 4 == 3)
            {
                //comando para encerrar o jogo depois de clicar em SAIR
                loop = 0;
            }
        }
    }

    endwin(); // finaliza o modo tela do ncurses
    return 0;
}
