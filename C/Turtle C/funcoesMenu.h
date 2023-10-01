#ifndef FUNCOESMENU_H_INCLUDED
#define FUNCOESMENU_H_INCLUDED

// retorna a metade do tamanho da sring
size_t metadetamanhostring(const char *str); // antigo divisaodois()

// inicializa��o da tela de menu
void ciMenu(WINDOW *win);

void escreveinstru(WINDOW *win, int alturay, int largurax);

void escrevecreditos(WINDOW *win, int alturay, int largurax);

void mainmenu(WINDOW *win, int alturay, int largurax);

void menumov(WINDOW *win, int alturay, int largurax, int opcao);

#endif // MENU_H_INCLUDED
