print('****************')
print('Bem vindo ao jogo de adivinhação!')
print('****************')

numero_secreto = 13

chute = input('Digite o seu numero: ')

print('Você digitou: ', chute_str)
chute = int(chute_str)
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print('Você acertou')
else:
    if(maior):
        print('Você errou! O seu chute foi maior do que o número secreto')
    elif(menor):
        print('Você erro! O seu chute foi menor do que o número secreto')

print('Fim do jogo')
print('************')



