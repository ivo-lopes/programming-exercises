#ifndef MENU_H_INCLUDED
#define MENU_H_INCLUDED

//retorna a metade do tamanho da sring
size_t metadetamanhostring(const char* str); //antigo divisaodois()

//inicialização da tela de menu
void ciMenu(WINDOW* win);

void escreveinstru(WINDOW* win,int alturay,int largurax);

void escrevecreditos(WINDOW* win,int alturay,int largurax);

void mainmenu(WINDOW* win,int alturay,int largurax);

void menumov(WINDOW* win,int alturay,int largurax,int opcao);


#endif // MENU_H_INCLUDED
