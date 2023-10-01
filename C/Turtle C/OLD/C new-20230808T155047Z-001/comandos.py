comandos = []
janela = []


#Input
entrada = comandos.getstr(0, 0)

#exceção caso o jogador queira voltar ao menu
if entrada.decode('utf-8') == 'sair':
    janela.clear()
    wrapper(inicio)

#Divisão do input     
dados = re.match(r'^(\S+)\s+(\d+)$', entrada.decode('utf-8'))

#Análise do input 
if entrada.decode('utf-8') == 'apagar':
    janela.clear()
    janela.box()
    janela.addstr(y,x,turtle)
    janela.refresh()

elif dados:
    direcao = dados.group(1)
    numeroPassos = int(dados.group(2))

#Movimentação baseada na direção e numero de passos
    if (direcao == "l" or direcao == "leste" ):
        for i in range(0,numeroPassos):    
            movimento()
            x+= 1
            if(x == largura-1):
                x = 1
    elif(direcao == "o" or direcao == "oeste"):
        for i in range(0,numeroPassos):                
            movimento()
            x-= 1
            if(x == 0):
                x = largura-2

    elif(direcao == "s" or direcao == "sul" ):
        for i in range(0,numeroPassos):
            movimento()
            y+= 1
            if(y == altura-7):
                y = 1

    elif(direcao == "n" or direcao == "norte"):
        for i in range(0,numeroPassos):                
            movimento()
            y-= 1
            if (y == 0):
                y = altura-8

    elif(direcao == "ne" or direcao == "nordeste" ):
        for i in range(0,numeroPassos):
            movimento()
            y-= 1
            x+= 1
            if (y == 0 ):
                y = altura-8  
            if(x == largura-1):
                x = 1

    elif(direcao == "no" or direcao == "noroeste"):
        for i in range(0,numeroPassos):
            movimento()
            y-= 1
            x-= 1
            if (y == 0 ):
                y = altura-8  
            if(x == 0):
                x = largura-2

    elif(direcao == "se" or direcao == "sudeste" ):
        for i in range(0,numeroPassos):
            movimento()
            y+= 1
            x+= 1
            if (y == altura-7 ):
                y = 1  
            if(x == largura-1):
                x = 1

    elif(direcao == "so" or direcao == "sudoeste"):
        for i in range(0,numeroPassos):
            movimento()
            y+= 1
            x-= 1
            if (y == altura-7 ):
                y = 1  
            if(x == 0):
                x = largura-2   

    #alteração do modo
    elif(direcao == "modo"):
        if (numeroPassos == 1):
            modo = 1
            turtle ="@"
        elif(numeroPassos == 2):
            modo = 2
            turtle = "#"
        if (modo == 1):
            teclamov = "*"
        elif(modo == 2):
            teclamov = " " 
#comando para fazer o fractal baseado no tamanho dado pelo número de passos. 
    elif(direcao == "fractal" or direcao == "fra"):
        for i in range(0,numeroPassos):
            movimento()
            y-= 1
            x+= 1
            if (y == 0 ):
                y = altura-8  
            if(x == largura-1):
                x = 1
        for i in range(0,numeroPassos):
            movimento()
            y+= 1
            x+= 1
            if (y == altura-7 ):
                y = 1  
            if(x == largura-1):
                x = 1
        for i in range(0,2*numeroPassos):
            movimento()
            x-= 1
        for i in range(0,numeroPassos):
            movimento()
            y+= 1
            x-= 1
            if (y == altura-7 ):
                y = 1  
            if(x == 0):
                x = largura-2  
        for i in range(0,2*numeroPassos):
            movimento()
            x+= 1
            if(x == largura-1):
                x = 1
        for i in range(0,numeroPassos):
            movimento()
            x-= 1
            y-= 1
            if (y == 0 ):
                y = altura-8  
            if(x == 0):
                x = largura-2
        for i in range(0,numeroPassos):
            movimento()
            x+= 1
            y+= 1
            if (y == altura-7 ):
            if (y == altura-7 ):
                y = 1  
            if(x == largura-1):
                x = 1                        
        for i in range(0,numeroPassos):
            movimento()
            x+=1
            y-=1
            if (y == 0 ):
                y = altura-8  
            if(x == largura-1):
                x = 1
        for i in range(0,numeroPassos):
            movimento()
            x+=1
            y+=1
            if (y == altura-7 ):
                y = 1  
            if(x == largura-1):
                x = 1
        for i in range(0,2*numeroPassos):
            movimento()
            x-= 1 
            if(x == 0):
                x = largura-2
#Comando para fazer um quadrado
    elif(direcao == "quadrado" or direcao == "quad"):
        for i in range(0,numeroPassos):
            movimento()
            y-= 1
            if (y == 0):
                y = altura-8
        for i in range(0,2*numeroPassos):
            movimento()
            x+= 1
            if(x == largura-1):
                x = 1
        for i in range(0,numeroPassos):
            movimento()
            y+=1
            if(y == altura-7):
                y = 1
        for i in range(0,2*numeroPassos):
            movimento()
            x-=1
            if(x == 0):
                x = largura-2
#Comando para fazer um triângulo
    elif(direcao == "triangulo" or direcao =="tri"):
        for i in range(0,numeroPassos):
            movimento()
            x+=1
            y-=1
            if (y == 0 ):
                    y = altura-8  
            if(x == largura-1):
                    x = 1
        for i in range(0,numeroPassos):
            movimento()
            x+=1
            y+=1
            if (y == altura-7 ):
                y = 1  
            if(x == largura-1):
                x = 1
        for i in range(0,2*numeroPassos):
            movimento()
            x-=1
            if(x == 0):
                x = largura-2
#comando para fazer um hexagono
    elif(direcao == "hexagono" or direcao == "hexa"):
        for i in range(0,2*numeroPassos):
            movimento()
            x+= 1
            if(x == largura-1):
                x = 1
        for i in range(0,numeroPassos):
            movimento()
            x+=1
            y+=1
            if (y == altura-7 ):
                y = 1  
            if(x == largura-1):
                x = 1
        for i in range(0,numeroPassos):
            movimento()
            x-=1
            y+=1
            if (y == altura-7 ):
                y = 1  
            if(x == 0):
                x = largura-2  
        for i in range(0,2*numeroPassos):
            movimento()
            x-=1
            if(x == 0):
                x = largura-2
        for i in range(0,numeroPassos):
            movimento()
            x-=1
            y-=1
            if (y == 0 ):
                    y = altura-8  
            if(x == 0):
                    x = largura-2
        for i in range(0,numeroPassos):
            movimento()
            x+=1
            y-=1
            if (y == 0 ):
                    y = altura-8  
            if(x == largura-1):
                    x = 1         
#comando para desenhar uma estrelar
    elif(direcao == "estrela" or direcao == "star"):
        for i in range(0,numeroPassos):
            movimento()    
            x+=1
            y-=1
            if (y == 0 ):
                y = altura-8  
            if(x == largura-1):
                x = 1
        for i in range(0,numeroPassos):
            movimento()
            x+=1
            y+=1   
            if (y == altura-7 ):
                y = 1  
            if(x == largura-1):
                x = 1 
        for i in range(0,(numeroPassos*2)):
            movimento()
            x+=1
            if(x == largura-1):
                x = 1
        for i in range(0,numeroPassos):
            movimento()
            x-=1
            y+=1
            if (y == altura-7 ):
                y = 1  
            if(x == 0):
                x = largura-2   
        for i in range(0,numeroPassos):
            movimento()
            x+=1
            y+=1
            if (y == altura-7 ):
                y = 1  
            if(x == largura-1):
                x = 1
        for i in range(0,(numeroPassos*2)):
            movimento()
            x-=1
            if(x == 0):
                x = largura-2
        for i in range(0,numeroPassos):
            movimento()
            x-=1
            y+=1
            if (y == altura-7 ):
                y = 1  
            if(x == 0):
                x = largura-2   
        for i in range(0,numeroPassos):
            movimento()
            x-=1
            y-=1
            if (y == 0 ):
                y = altura-8  
            if(x == 0):
                x = largura-2
        for i in range(0,(numeroPassos*2)):
            movimento()
            x-=1
            if(x == 0):
                x = largura-2
        for i in range(0,numeroPassos):
            movimento()
            x+=1
            y-=1
            if (y == 0 ):
                y = altura-8  
            if(x == largura-1):
                x = 1
        for i in range(0,numeroPassos):
            movimento()
            x-=1
            y-=1
            if (y == 0 ):
                y = altura-8  
            if(x == 0):
                x = largura-2
        for i in range(0,(numeroPassos*2)):
            movimento()
            x+=1
            if(x == largura-1):
                x = 1

            
#É impresso "ERROR" na tela de comandos caso o que o usuário tenha digitado não corresponda a nenhuma outra entrada admitida pelo jogo
    else:
        limpeza(comandos)
        comandos.addstr(0,0,"ERROR")
        comandos.refresh()
        comandos.getch() 
    
else :
    limpeza(comandos)
    comandos.addstr(0,0,"ERROR")
    comandos.refresh()
    comandos.getch()
