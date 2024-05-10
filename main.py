#Pedro Augusto Nalin Tronco
#RA: 1136278
from func import titulo,help,limparTela,pause,corTitulo,corCompetidor,corDesafiante,abrirHistorico,estagioForca,mostrarDica,vitoria,gameOver,salvarHistorico
try:
    arquivo=open("historico.JogoDaForca","r",encoding="utf-8")
    arquivo.close
except:
    arquivo=open("historico.JogoDaForca","w",encoding="utf-8")
    arquivo.write("")
    arquivo.close
while True:
    mainLooping=True
    checkGabarito=True
    checkTentativa=True
    acerto=False
    palavraChave=[]
    letrasUsadas=[]
    erros=0
    dicas=0
    tentativa=""
    gabarito=""
    while True:
        limparTela()
        corTitulo()
        titulo()
        print("Bem vindo ao Jogo da Forca!")
        print("Digite '1' para ajuda")
        print("Digite '2' para começar")
        print("Digite '3' para abrir o histórico")
        print("Digite '4' para deletar o histórico.")
        print("Digite '5' para sair")
        comeco=input()
        if comeco=="1":
            help()
        elif comeco=="2":
            break
        elif comeco=="3":
            abrirHistorico()
        elif comeco=="4":
            arquivo=open("historico.JogoDaForca","w",encoding="utf-8")
            arquivo.write("")
            arquivo.close
            print("Histórico deletado com sucesso.")
            pause()
        elif comeco=="5":
            limparTela()
            print("Obrigado por jogar!")
            quit()
        else:
            print(f"'{comeco}' é um comando inválido.")
            pause()

    limparTela()
    corDesafiante()
    desafiante=input("Insira o nome do desafiante: ")
    limparTela()
    corCompetidor()
    competidor=input("Insira o nome do competidor: ")

    limparTela()
    corDesafiante()
    while True:
        print("Insira a palavra ou frase a ser adivinhada (sem acento). Em caso de múltiplas palavras, separe-as por espaço. ")
        palavraCheck=True
        gabarito=input()
        try:
            gabarito=gabarito.upper()
            for caracter in gabarito:
                if caracter.isnumeric():
                    palavraCheck=False
            if gabarito.isascii() and len(gabarito)>0 and palavraCheck:
                break
            else:
                2/0
        except:
            print("Erro! A palavra não deve conter números ou caractéres especiais")

    limparTela()
    print(f"A palavra é '{gabarito}'. Agora insira 3 dicas para auxíliar o competidor.")
    dica1=input("Insira a primeira dica: ")
    dica2=input("Insira a segunda dica: ")
    dica3=input("Insira a terceira dica: ")

    for caracter in gabarito:
        if caracter != " ":
            palavraChave.append("_")
        else:
            palavraChave.append(" ")

    limparTela()
    corCompetidor()
    while mainLooping:
        while True: 
            limparTela()
            estagioForca(erros)
            print(" ".join(palavraChave))
            print()
            print(f"Letras usadas: {letrasUsadas}")
            print(f"Dicas usadas: {dicas}/3")
            print()
            print("Digite '!' para receber uma dica")
            print("Digite uma letra para fazer uma tentativa")
            tentativa=input()
            if tentativa=="!":
                mostrarDica(dicas,dica1,dica2,dica3)
                if dicas<3: dicas+=1
                pause()
            elif tentativa.isalpha() and len(list(tentativa))==1:
                tentativa=tentativa.upper()
                if tentativa in letrasUsadas:
                    print(f"Você já tentou a letra {tentativa}!")
                    pause()
                else:break
            else:
                print("Erro! Digite apenas uma letra minúscula")
                pause()
        posicao=0
        acerto=False
        for letra in gabarito:
            if tentativa==letra:
                palavraChave[posicao]=letra
                acerto=True
            posicao+=1
        if acerto==False:
            erros+=1
            letrasUsadas.append(str(tentativa))
            print(f"Não há '{tentativa}' na palavra.")
            pause()
        if palavraChave==list(gabarito):
            vitoria(competidor,dicas,len(letrasUsadas))
            mainLooping=False
            salvarHistorico(competidor,desafiante,dicas,letrasUsadas,gabarito,competidor)
        elif erros>5:
            corDesafiante()
            gameOver(desafiante,gabarito,len(letrasUsadas))
            mainLooping=False
            salvarHistorico(competidor,desafiante,dicas,letrasUsadas,gabarito,desafiante)
