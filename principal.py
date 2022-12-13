
import os

palavra_secreta = 'pedrita'
letras_acertadas = ''
numero_tentativas = len(palavra_secreta)

print('*****************************************************************************')
print('*************************BEM VINDO AO JOGO DA FORCA!*************************')
print('*****************************************************************************')

while True:
    letra_digitada = input('Digite uma Letra: ')
    letra_digitada = letra_digitada.lower()

    if len(letra_digitada) > 1:
        print('Só é permitido digitar uma letra por Tentativa.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    if letra_digitada not in palavra_secreta:
        numero_tentativas -= 1
        print('Você possui: ', numero_tentativas, 'Tentativas')

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '_'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavara secreta era: ', palavra_secreta.upper())
        print('Tentativas: ', numero_tentativas)

    if numero_tentativas == 0:
        print('VOCÊ PERDEU!!!')
        print('A PALAVRA SECRETA ERA: ', palavra_secreta.upper())
        break