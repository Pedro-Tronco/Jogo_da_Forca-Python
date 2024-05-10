import os

def limparTela():
    os.system("cls")

def corDesafiante():
    os.system("color 8")

def corCompetidor():
    os.system("color F")

def corTitulo():
    os.system("color 2")

def pause():
    input("Aperte 'enter' para prosseguir")

def abrirHistorico():
    try:
        arquivo=open("historico.JogoDaForca","r",encoding="utf-8")
        arquivo.close()
    except:
        arquivo=open("historico.JogoDaForca","w",encoding="utf-8")
        arquivo.write("")
        arquivo.close()
    arquivo=open("historico.JogoDaForca","r",encoding="utf-8")
    dados=arquivo.read()
    if dados=="":
        print("O Histórico está vazio.")
        pause()
    else:
        print()
        print(dados)
        arquivo.close()
        pause()

def titulo():
    print("""
   oooo                                           .o8                 oooooooooooo                                        
   `888                                          "888                 `888'     `8                                        
    888  .ooooo.   .oooooooo  .ooooo.        .oooo888   .oooo.         888          .ooooo.  oooo d8b  .ooooo.   .oooo.   
    888 d88' `88b 888' `88b  d88' `88b      d88' `888  `P  )88b        888oooo8    d88' `88b `888""8P d88' `"Y8 `P  )88b  
    888 888   888 888   888  888   888      888   888   .oP"888        888    "    888   888  888     888        .oP"888  
    888 888   888 `88bod8P'  888   888      888   888  d8(  888        888         888   888  888     888   .o8 d8(  888  
.o. 88P `Y8bod8P' `8oooooo.  `Y8bod8P'      `Y8bod88P" `Y888""8o      o888o        `Y8bod8P' d888b    `Y8bod8P' `Y888""8o 
`Y888P            d"     YD                                                                                               
                  "Y88888P'                                                                                               
                                                                                                                         
""")

def help():
    print("""
Esse é um pequeno Jogo da Forca para 2 jogadores escrito dentro de python. 
              
O jogador 1, chamado de Desafiante é aquele que escolherá a palavra a ser advinhada. A cor de seu texto é cinza. 

Já o jogador 2, chamado de Competidor, é aquele que tem que adivinhar a palavra dentro de 6 tentativas. Seu texto é branco.
              
O jogo começa com os dois participantes inserindo seu nome. Então, o Desafiante deve escolher a palavra que será usada,
de acordo com os parametros escritos, e também deve atribuír 3 dicas para auxiliar o Competidor, caso este ache necessário.
Então, o Competidor deve tentar descobrir as palavras letra por letra, usando o mínimo de dicas possível. No final
do jogo, apos os dois jogadores terem se revezado entre Desafiante e Competidor, ganha aquele que acertou a palavra
enquanto Competidor com menos dicas utilizadas. Para um último desempate, use as tentativas de letras erradas.
    """)
    pause()

def gameOver(desafiante,gabarito,quantiaErros):
    limparTela()
    corDesafiante()
    print("""
oooooooooo.   oooooooooooo ooooooooo.   ooooooooo.     .oooooo.   ooooooooooooo       .o.       
`888'   `Y8b  `888'     `8 `888   `Y88. `888   `Y88.  d8P'  `Y8b  8'   888   `8      .888.      
 888      888  888          888   .d88'  888   .d88' 888      888      888          .8"888.     
 888      888  888oooo8     888ooo88P'   888ooo88P'  888      888      888         .8' `888.    
 888      888  888    "     888`88b.     888`88b.    888      888      888        .88ooo8888.   
 888     d88'  888       o  888  `88b.   888  `88b.  `88b    d88'      888       .8'     `888.  
o888bood8P'   o888ooooood8 o888o  o888o o888o  o888o  `Y8bood8P'      o888o     o88o     o8888o
""")
    print(f"{desafiante} venceu! A palavra era '{gabarito}'.")
    print()
    estagioForca(quantiaErros)

def vitoria(competidor,dicas,quantiaErros):
    limparTela()
    corCompetidor()
    print("""
oooooo     oooo ooooo ooooooooooooo   .oooooo.   ooooooooo.   ooooo       .o.       
 `888.     .8'  `888' 8'   888   `8  d8P'  `Y8b  `888   `Y88. `888'      .888.      
  `888.   .8'    888       888      888      888  888   .d88'  888      .8"888.     
   `888. .8'     888       888      888      888  888ooo88P'   888     .8' `888.    
    `888.8'      888       888      888      888  888`88b.     888    .88ooo8888.   
     `888'       888       888      `88b    d88'  888  `88b.   888   .8'     `888.  
      `8'       o888o     o888o      `Y8bood8P'  o888o  o888o o888o o88o     o8888o
""")
    print(f"{competidor} venceu usando {dicas}/3 dicas e com {quantiaErros} letras erradas!")
    print()
    estagioForca(quantiaErros)

def salvarHistorico(competidor,desafiante,dicas,letrasUsadas,gabarito,vencedor):
    while True:
        print("Você deseja salvar esse jogo no Histórico?")
        print("Digite 's' para sim")
        print("Digite 'n' para não")
        check=input()
        if check=="s":
            try:
                arquivo=open("historico.JogoDaForca","r",encoding="utf-8")
                arquivo.close()
            except:
                arquivo=open("historico.JogoDaForca","w",encoding="utf-8")
                arquivo.write("")
                arquivo.close()
            arquivo=open("historico.JogoDaForca","a",encoding="utf-8")
            arquivo.write(f"{desafiante} x {competidor} : {vencedor} venceu. \n   Palavra: {gabarito} \n   Quantia de Erros: {len(letrasUsadas)} \n   Letras usadas: {letrasUsadas} \n   Dicas utilizadas: {dicas}/3 \n \n")
            arquivo.close()
            print("Jogo adicionado com sucesso!")
            input("Aperte 'enter' para recomeçar")
            break
        elif check=="n":
            print("O jogo não foi salvo.")
            input("Aperte 'enter' para recomeçar")
            break
        else: print(f"Erro! '{check}' é um comando inválido.")

def mostrarDica(dicas,dica1,dica2,dica3):
    if dicas==0:
        print(f"Dica 1: {dica1}")
    elif dicas==1:
        print(f"Dica 2: {dica2}")
    elif dicas==2:
        print(f"Dica 3: {dica3}")
    else: 
        print("Dicas esgotadas!")

def estagioForca(erros):
    if erros==0:
        print("""
      ________
      |      |
      |
      |
      |
  ____|____
""")
    elif erros==1:
        print("""
      ________
      |      |
      |      O
      |
      |
  ____|____
""")
    elif erros==2:
        print("""
      ________
      |      |
      |      O
      |      |
      |
  ____|____
""")
    elif erros==3:
        print("""
      ________
      |      |
      |      O
      |     /|
      |
  ____|____
""")
    elif erros==4:
        print("""
      ________
      |      |
      |      O
      |     /|\ 
      |
  ____|____
""")
    elif erros==5:
        print("""
      ________
      |      |
      |      O
      |     /|\ 
      |     / 
  ____|____
""")
    else:
        print("""
      ________
      |      |
      |      O
      |     /|\ 
      |     / \ 
  ____|____
""")