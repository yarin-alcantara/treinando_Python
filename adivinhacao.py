import random

def jogar_adivinhacao():
    print('****************')
    print('Bem vindo ao jogo de Adivinhação!')
    print('****************')

    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000

    print('Escolha um nivel de difuldade: ')
    print('(1) Fácil, (2) Médio, (3) Dificil')

    nivel = int(input('Digite o número do nível: '))

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    print(numero_secreto)

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {} '.format(rodada, total_de_tentativas))
        chute_str = input('Digite o seu número de 1 a 100: ')
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1):
            print('Você deve digitar um número entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('Você acertou e fez {} pontos'.format(pontos))
            break
        else:
            if(maior):
                print('Você errou! O seu chute foi maior do que o número secreto')
            elif(menor):
                print('Você errou! O seu chute foi menor do que o número secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print('Fim do jogo')
    print('************')



