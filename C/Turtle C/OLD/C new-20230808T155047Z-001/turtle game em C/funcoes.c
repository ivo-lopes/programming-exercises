#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ncurses.h>
#include "funcoes.h"

int contDig(int a){
    int contador = 0;

    if (a == 0) {
        contador = 1;
    } else {
        int temp = a;
        while (temp != 0) {
            temp /= 10;
            contador++;
        }
    }
    return contador;
}

char* transfStr(int a){

    char* num = (char*)malloc(contDig(a)+1);
    if (a < 10){
        sprintf(num,"0%d",a);
    }else {
        sprintf(num,"%d",a);
    }
    return num;
}

char* coord(int dx,int dy){
    char* x = transfStr(dx);
    char* y = transfStr(dx);

    strcpy(x,transfStr(dx));
    strcpy(y,transfStr(dy));

    int tamanho = 9 + strlen(transfStr(dx)) + strlen(transfStr(dy));
    char* frase = (char*)malloc(tamanho+1);

    if(frase != NULL){
        sprintf(frase,"x,y = (%s,%s)",x,y);
    }


    return frase;

}

void limpeza(WINDOW *win) {


    werase(win);
    wrefresh(win);
}

void movimento (WINDOW* win, int y, int x, char teclaMov){
    mvwprintw(win, y , x , "%c", teclaMov);
}
