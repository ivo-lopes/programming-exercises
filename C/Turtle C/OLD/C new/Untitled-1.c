#include <ncurses.h>
#include <string.h>
#include <stdlib.h>

// Screen configuration definitions.
void ci(WINDOW *tela) {
    wclear(tela);
    curs_set(1);
    echo();
}

// Function to format coordinates below 10.
char* transfStr(int a) {
    char *str = malloc(3 * sizeof(char));
    if (a < 10) {
        sprintf(str, "0%d", a);
    } else {
        sprintf(str, "%d", a);
    }
    return str;
}

// Function that types the phrase indicating the current position of the turtle.
char* coord(char* dx, char* dy) {
    char *frase = malloc(15 * sizeof(char));
    sprintf(frase, "x,y = (%s,%s)", dx, dy);
    return frase;
}

// Function that creates the turtle movement window.
void criacaoJanela(int alturaJanela, int largura, int posicaox, int posicaoy) {
    WINDOW *janela = newwin(alturaJanela, largura, posicaox, posicaoy);
    box(janela, 0, 0);
    wrefresh(janela);
}

// Elements to be used directly in the game.
void elementosJogo(int turtle, int teclamov, int modo) {
    return;
}

// Function to clear the screen.
void limpeza(WINDOW *a) {
    werase(a);
    wrefresh(a);
}

void main(WINDOW *tela) {

    // Initial settings.
    ci(tela);

    // Declaration of variables related to windows and pads.
    int altura, largura;
    getmaxyx(tela, altura, largura);
    int margemInferior = 3;
    int margemSuperior = 3;
    int distanciaDigitaocao = 1;
    char *nomeComandos = "Direção :";

    // Values of the initial coordinates of the turtle.
    int x = (largura - 2) / 2;
    int y = (altura - margemInferior - margemSuperior) / 2;

    // Coordinate text.
    char *dx = transfStr(x);
    char *dy = transfStr(y);
    char *coordenadas = coord(dx, dy);
    char *vazio = "              ";

    // Establishment of window and pad measurements.
    int alturajanela = altura - margemInferior - margemSuperior;
    int larguracoord = strlen(coordenadas) + 3;

    int posicaoxComandos = strlen(nomeComandos) + distanciaDigitaocao;
    int larguraComando = largura - larguracoord - posicaoxComandos - 2;

    // Game elements.
    char turtle, teclamov;
    int modo;
    elementosJogo(turtle, teclamov, modo);

    // Creation of the character movement window.
    WINDOW *janela = newwin(alturajanela, largura, margemSuperior, 0);
    box(janela, 0, 0);
    wrefresh(janela);

    // Creation of the pad for the coordinates.
    WINDOW *padcoord = newpad(3, larguracoord);
    box(padcoord, 0, 0);
    mvwaddstr(padcoord, 1, 1, coordenadas);
    prefresh(padcoord, 0, 0, altura - margemInferior, largura - larguracoord, altura - 1, largura - 1);

    // Creation of pads for the command.
    WINDOW *padcom = newpad(margemInferior, largura - larguracoord - 1);
    mvwaddstr(padcom, 1, 1, nomeComandos);
    box(padcom, 0, 0);
    prefresh(padcom, 0, 0, altura - margemInferior , 0 , altura - 1 , largura - larguracoord - 1);

    // Creation of pad size.
    char *xTamanho = transfStr(largura-2);
    char *yTamanho = transfStr(alturajanela);
    char *tamanho = coord(xTamanho,yTamanho);

    // Pad mode.
    WINDOW *padmodo = newpad(3, 10);
    box(padmodo, 0, 0);
    prefresh(padmodo, 0, 0, 0, largura - 10, 3, largura - 1);

    // Creation of space for typing commands.
    WINDOW *comandos = newwin(1, larguraComando, altura - 2, posicaoxComandos);
}

while (1) {
    // Mode update.
    mvwaddstr(padmodo, 1, 1, "Modo: ");
    wprintw(padmodo, "%d", modo);
    prefresh(padmodo, 0, 0, 0, largura - 10, 3, largura - 1);

    // Coordinate update.
    dx = transfStr(x);
    dy = transfStr(y);

    // Printing of turtle coordinates.
    coordenadas = coord(dx, dy);
    mvwaddstr(padcoord, 1, 1, coordenadas);
    prefresh(padcoord, 0, 0, altura - 3, largura - larguracoord, altura - 1, largura - 1);
    if (x < 100) {
        mvwaddstr(padcoord, 1, 1, vazio);
        coordenadas = coord(dx, dy);
        mvwaddstr(padcoord, 1, 1, coordenadas);
        prefresh(padcoord, 0, 0, altura - 3, largura - larguracoord, altura - 1, largura - 1);
    }
    if (y < 100) {
        mvwaddstr(padcoord, 1, 1, vazio);
        coordenadas = coord(dx, dy);
        mvwaddstr(padcoord, 1, 1, coordenadas);
        prefresh(padcoord, 0, 0, altura - 3, largura - larguracoord, altura - 1, largura - 1);
    }