#ifndef FUNCOESJOGO_H_INCLUDED
#define FUNCOESJOGO_H_INCLUDED

int contDig(int a);

char *transfStr(int a);

char *coord(int dx, int dy);

void limpeza(WINDOW *a);

void movimento(WINDOW *win, int y, int x, char teclaMov);

#endif // FUNCOESJOGO_H_INCLUDED
