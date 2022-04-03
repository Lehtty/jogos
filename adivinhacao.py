import random

def jogar():

    print("                                           ")
    print("*****Bem vindo ao jogo de Adivinhação!*****")
    print("                                           ")

    numero_secreto = random.randrange(1,101)
    total_de_vezes = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha de dificuldade: "))

    if(nivel == 1):
        total_de_vezes =20
    elif(nivel == 2):
        total_de_vezes = 10
    else:
        total_de_vezes = 5

    for rodada in range(1, total_de_vezes + 1):
        print("Tentativa: {} de {}". format(rodada, total_de_vezes))
        chutenumero = input("Digite o seu numero: ")
        print("Você digitou ", chutenumero)
        chute = int(chutenumero)

        if(chute < 1 or chute > 100):
            print("O numero deve ser entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (acertou):
            print(f"Acerto miseraví, você fez {pontos} pontos!")
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o numero secreto")
                if (rodada == total_de_vezes):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")
            elif(menor):
                print("Você errou! O seu chute foi menor que o numero secreto")
                if (rodada == total_de_vezes):
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("                        ")
    print("******Fim de jogo!******")
    print("                        ")

if(__name__ == "__main__"):
    jogar()