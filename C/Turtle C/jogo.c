#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ncurses.h>
#include "funcoesJogo.h"


int main()
{

    // Configura��es iniciais
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);

    // Declara��o das variaveis relacionadas as janelas e pads
    int altura, largura;
    getmaxyx(stdscr, altura, largura);
    int margemSuperior = 3;
    int margemInferior = 3;
    int distanciaDigitacao = 1;
    char nomeComandos[] = "Comando --> ";
    char input[50];
    char direcao[10];
    int passos;
    int ch;
    int i = 0;
    const char *direcoes_validas[] = {"n", "s", "l", "o", "ne", "no", "se", "so"};

    // Valores das coordenadas iniciais da tartaruga
    int x = (largura - 2) / 2;
    int y = (altura - margemInferior - margemSuperior) / 2;

    // Texto das coordenadas iniciais da tartagura
    char *coordenadas = (char *)malloc(sizeof(coord(x, y) + 1));
    if (coordenadas != NULL)
    {
        strcpy(coordenadas, coord(x, y));
    }

    // Estabelecimento das medidas das janelas e pads

    int alturaJanela = altura - margemInferior - margemSuperior;
    int larguraCoord = (int)(strlen(coord(largura - 2, alturaJanela)) + 2);

    int posicaoxComandos = sizeof(nomeComandos) + distanciaDigitacao;
    int larguraComando = largura - larguraCoord - posicaoxComandos - 2;

    // Elementos do Jogo
    char turtleModo = '@';
    char teclaMov = '*';
    int modo = 1;

    // Cria��o da janela para movimenta��o do personagem
    WINDOW *win = newwin(alturaJanela, largura, margemSuperior, 0);
    box(win, 0, 0);
    wrefresh(win);

    // Cria��o pad tamanho obs: problema no uso do coord

    char *tamanho = coord(largura - 2, alturaJanela); // resolver problema de coord pedir como parametro int
    WINDOW *padTamanho = newpad(3, (int)(strlen(tamanho) + 2));
    box(padTamanho, 0, 0);

    // Cria��o do pad para as coordenadas
    WINDOW *padCoord = newpad(3, larguraCoord);
    box(padCoord, 0, 0);

    // Cria��o dos pads para o comando
    WINDOW *padCom = newpad(margemInferior, largura - larguraCoord - 1);
    box(padCom, 0, 0);
    mvwprintw(padCom, 1, 1, "%s", nomeComandos);
    prefresh(padCom, 0, 0, altura - margemInferior, 0, altura - 1, largura - larguraCoord - 1);

    mvwprintw(padTamanho, 1, 1, "%s", tamanho);
    prefresh(padTamanho, 0, 0, 0, 0, 3, largura - 1);

    // pad modo

    WINDOW *padModo = newpad(3, 10);
    box(padModo, 0, 0);
    prefresh(padModo, 0, 0, 0, largura - 10, 3, largura - 1);

    // Cria��o do espa�o para a digita��o dos comandos
    WINDOW *comandos = newwin(1, larguraComando, altura - 2, posicaoxComandos);

    while (1)
    {
        // atualiza��o do modo
        mvwprintw(padModo, 1, 1, "Modo: %d", modo);
        prefresh(padModo, 0, 0, 0, largura - 10, 3, largura - 1);

        // atualiza��o das coordenadas
        werase(padCoord);
        box(padCoord, 0, 0);
        mvwprintw(padCoord, 1, 1, "%s", coord(x, y));
        prefresh(padCoord, 0, 0, altura - margemInferior, largura - larguraCoord, altura - 1, largura - 1);

        // impress�o da turtle
        mvwprintw(win, y, x, "%c", turtleModo);
        wrefresh(win);

        limpeza(comandos);

        // input
        mvwgetstr(comandos, 0, 0, input);
        input[strcspn(input, "\n")] = '\0'; // Remover o caractere de nova linha
        //fim input



        if (strcmp(input, "sair") == 0)
        {
            // fazer o sair
            break;
        }
        else if (strcmp(input, "apagar") == 0)
        {

            // fazer o apagar
        }
        else if (strncmp(input, "modo", 4) == 0)
        {
            modo = atoi(input + 4); // Extrai o numero apos "modo"
            if (modo == 1 || modo == 2)
            {
                if (modo == 1)
                {
                    turtleModo = "@";
                    teclaMov = "*";
                }
                else if (modo == 2)
                {
                    turtleModo = "#";
                    teclaMov = " ";
                }
            }
            else
            {
                limpeza(comandos);
                wgetch(comandos);
            }
        }
        else if (sscanf(input, "%9[a-z] %d", direcao, &passos) == 2)
        {
            int direcao_valida = 0;
            for (int i = 0; i < sizeof(direcoes_validas) / sizeof(direcoes_validas[0]); i++)
            {
                if (strcmp(direcao, direcoes_validas[i]) == 0)
                {
                    direcao_valida = 1;
                    break;
                }
            }

            if (direcao_valida)
            {
                printf("Dire��o: %s\n", direcao);
                printf("Passos: %d\n", passos);
            }
            else
            {
                limpeza(comandos);
                wgetch(comandos);
            }
        }
        else
        {
            limpeza(comandos);
            wgetch(comandos);
        }

        if (strcmp(direcao, "l") == 0 || strcmp(direcao, "leste") == 0)
        {
            for (int i = 0; i < passos; i++)
            {
                movimento(win, y, x, teclaMov);
                x += 1;
                if (x == largura - 1)
                {
                    x = 1;
                }
            }
        }
        else if (strcmp(direcao, "o") == 0 || strcmp(direcao, "oeste") == 0)
        {
            for (int i = 0; i < passos; i++)
            {
                movimento(win, y, x, teclaMov);
                x -= 1;
                if (x == 0)
                {
                    x = largura - 2;
                }
            }
        }
        else if (strcmp(direcao, "s") == 0 || strcmp(direcao, "sul") == 0)
        {
            for (int i = 0; i < passos; i++)
            {
                movimento(win, y, x, teclaMov);
                y += 1;
                if (y == altura - 7)
                {
                    y = 1;
                }
            }
        }
        else if (strcmp(direcao, "n") == 0 || strcmp(direcao, "norte") == 0)
        {
            for (int i = 0; i < passos; i++)
            {
                movimento(win, y, x, teclaMov);
                y -= 1;
                if (y == 0)
                {
                    y = altura - 8;
                }
            }
        }
        else if (strcmp(direcao, "ne") == 0 || strcmp(direcao, "nordeste") == 0)
        {
            for (int i = 0; i < passos; i++)
            {
                movimento(win, y, x, teclaMov);
                y -= 1;
                x += 1;
                if (y == 0)
                {
                    y = altura - 8;
                }
                if (x == largura - 1)
                {
                    x = 1;
                }
            }
        }
        else if (strcmp(direcao, "no") == 0 || strcmp(direcao, "noroeste") == 0)
        {
            for (int i = 0; i < passos; i++)
            {
                movimento(win, y, x, teclaMov);
                y -= 1;
                x -= 1;
                if (y == 0)
                {
                    y = altura - 8;
                }
                if (x == 0)
                {
                    x = largura - 2;
                }
            }
        }
        else if (strcmp(direcao, "se") == 0 || strcmp(direcao, "sudeste") == 0)
        {
            for (int i = 0; i < passos; i++)
            {
                movimento(win, y, x, teclaMov);
                y += 1;
                x += 1;
                if (y == altura - 7)
                {
                    y = 1;
                }
                if (x == largura - 1)
                {
                    x = 1;
                }
            }
        }
        else if (strcmp(direcao, "so") == 0 || strcmp(direcao, "sudoeste") == 0)
        {
            for (int i = 0; i < passos; i++)
            {
                movimento(win, y, x, teclaMov);
                y += 1;
                x -= 1;
                if (y == altura - 7)
                {
                    y = 1;
                }
                if (x == 0)
                {
                    x = largura - 2;
                }
            }
        }
        wgetch(win);
    }
    // Limpar a janela e finalizar
    free(coordenadas);
    wclear(win);
    wrefresh(win);
    delwin(win);
    endwin();
    return 0;
}
