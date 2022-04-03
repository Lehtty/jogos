import forca
import adivinhacao

def escolha_de_jogos():
    print("                ")
    print("****************")
    print("Escolha um jogo!")
    print("****************")
    print("                ")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo você quer? "))

    if(jogo == 1):
        print("Você escolheu jogo da forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Você escolheu o jogo de adivinhação!")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_de_jogos()