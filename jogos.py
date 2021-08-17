import adivinhacao
import forca

print('****************')
print('Escolha um jogo!')
print('****************')

print('Digite (1) Adivinhação (2) Forca')

jogo = int(input('Digite o número do jogo escolhido: '))
if(jogo == 1):
    print('Vamos jogar adivinhação')
    adivinhacao.jogar_adivinhacao()
elif(jogo == 2):
    print('Vamos jogar Forca')
    forca.jogar_forca()
