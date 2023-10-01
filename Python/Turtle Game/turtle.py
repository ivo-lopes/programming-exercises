import curses
from curses import wrapper
import re

def ci(tela):
    tela.clear()
    curses.curs_set(1)
    curses.echo()

def transfStr(a):
    if (a < 10) :
        return "0" + str(a)
    else : 
        return str(a)

def coord(dx,dy):
    frase = "x,y = (" + dx + "," + dy + ")"
    return frase

def criacaoJanela(alturaJanela,largura,posicaox,posicaoy,bordaLateral,bordaFrontal):
    janela = curses.newwin(alturaJanela,largura,posicaox,posicaoy)
    janela.box(bordaLateral,bordaFrontal)
    janela.refresh()
    
def elementosJogo(turtle,bordaLateral,bordaFrontal,teclamov,modo):
    return (turtle,bordaLateral,bordaFrontal,teclamov,modo)    

def limpeza(a):
            a.erase()
            a.refresh()  

def main(tela):

    #configurações iniciais
    ci(tela)

    #Declaração das variaveis relacionadas as janelas e pads
    altura,largura = tela.getmaxyx()
    margemInferior = 3 
    margemSuperior = 3
    distanciaDigitaocao = 1

    #Valores das coordenadas iniciais da tataruga
    x = largura//2  
    y = (altura-margemInferior)//2

    
    #Transformação de int em str
    dx = transfStr(x)
    dy = transfStr(y)

    coordenadas = coord(dx,dy)

    nomeComandos = "Direção :"
    
    #Estabelecimento das medidas das janelas e pads
   
    alturajanela = altura-margemInferior-margemSuperior
    larguracoord = len(coordenadas)+2
    
    posicaoxComandos = len(nomeComandos) + distanciaDigitaocao
    larguraComando = largura-larguracoord-posicaoxComandos-2

    #Elementos do jogo
    turtle,bordaLateral,bordaFrontal,teclamov,modo = elementosJogo("@","|","-","*",1)

    #Criação da janela de movimentação do personagem
    janela = curses.newwin(alturajanela,largura,margemSuperior,0)
    janela.box(bordaLateral,bordaFrontal)
    janela.refresh()

    #Criação do pad para as coordenadas
    padcoord = curses.newpad(3,larguracoord)
    padcoord.box(bordaLateral,bordaFrontal)
    padcoord.addstr(1,1,coordenadas)
    padcoord.refresh(0,0,altura-margemInferior,largura-larguracoord,altura-1,largura-1)

    #Criação dos pads para o comando
    padcom = curses.newpad(margemInferior,largura-larguracoord-1)
    padcom.addstr(1,1,nomeComandos)
    padcom.box(bordaLateral,bordaFrontal)
    padcom.refresh(0, 0, altura-margemInferior , 0 , altura-1 , largura-larguracoord-1)

    #
    xTamanho = transfStr(largura-2)
    yTamanho = transfStr(alturajanela)
    tamanho = coord(xTamanho,yTamanho)

    #Criação pad tamanho
    padtamanho = curses.newpad(3,len(tamanho)+2)
    padtamanho.box(bordaLateral,bordaFrontal)
    padtamanho.addstr(1,1,tamanho)
    padtamanho.refresh(0,0,0,0,3,largura-1)
    
    #pad modo
    padmodo = curses.newpad(3,10)
    padmodo.box(bordaLateral,bordaFrontal)
    padmodo.refresh(0,0,0,largura-10,3,largura-1)

    #Criação do espaço para digitação dos comandos
    comandos = curses.newwin(1,larguraComando,altura-2,posicaoxComandos)

    while True: 
        #atualização do modo
        padmodo.addstr(1,1,f"Modo: {modo}")
        padmodo.refresh(0,0,0,largura-10,3,largura-1)

        #atualização das coordenadas
        dx = transfStr(x)
        dy = transfStr(y)

        #impressão das coordenadas do turtle
        coordenadas = coord(dx,dy)
        padcoord.addstr(1,1,coordenadas)
        padcoord.refresh(0,0,altura-3,largura-larguracoord,altura-1,largura-1)    

        #impressão do turtle
        janela.addstr(y,x,turtle)
        janela.refresh()
        
        limpeza(comandos)
        
        #Entradas
        entrada = comandos.getstr(0, 0)
        dados = re.match(r'^(\S+)\s+(\d+)$', entrada.decode('utf-8'))
        
        #Divisão da entrada em dois grupos
        if dados:
            direcao = dados.group(1)
            numeroPassos = int(dados.group(2))
            
        #Função que irá printar a atual localização em y,x
        def movimento():
            janela.addstr(y,x,teclamov)
        
        #Movimentação baseada na direção e numero de passos
        try :
            if (direcao == "leste" ):  
                for i in range(0,numeroPassos):    
                    movimento()
                    x+= 1
                    if(x == largura-1):
                        x = 1
            elif(direcao == "oeste" ):
                for i in range(0,numeroPassos):                
                    movimento()
                    x-= 1
                    if(x == 0):
                        x = largura-1

            elif(direcao == "sul" ):
                for i in range(0,numeroPassos):
                    movimento()
                    y+= 1
                    if(y == altura-7):
                        y = 1

            elif(direcao == "norte" ):
                for i in range(0,numeroPassos):                
                    movimento()
                    y-= 1
                    if (y == 0):
                        y = altura-8

            elif(direcao == "nordeste" ):
                for i in range(0,numeroPassos):
                    movimento()
                    y-= 1
                    x+= 1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == largura-2):
                        x = 1
            elif(direcao == "noroeste" ):
                for i in range(0,numeroPassos):
                    movimento()
                    y-= 1
                    x-= 1
                    if (y == 0 ):
                        y = altura-8  
                    if(x == 0):
                        x = largura-2
            elif(direcao == "sudeste" ):
                for i in range(0,numeroPassos):
                    movimento()
                    y+= 1
                    x+= 1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == largura-2):
                        x = 1
            elif(direcao == "sudoeste" ):
                for i in range(0,numeroPassos):
                    movimento()
                    y+= 1
                    x-= 1
                    if (y == altura-7 ):
                        y = 1  
                    if(x == 0):
                        x = largura-2   
            elif(direcao == "modo"):
                if (numeroPassos == 1):
                    modo = 1
                elif(numeroPassos == 2):
                    modo = 2
                if (modo == 1):
                    teclamov = "*"
                elif(modo == 2):
                    teclamov = " "   
        except : ValueError
        comandos.addstr(0,0,"erro!!")
        comandos.refresh()
        comandos.getch()

wrapper(main)