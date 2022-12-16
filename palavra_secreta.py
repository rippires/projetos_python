import random


def carrega_palavra_secreta():


    palavras = open('palavras.txt', 'r')
    palavra = []

    for linha in palavras:
        linha = linha.strip()
        palavra.append(linha)
        

    palavras.close()

    numero = random.randrange(0, len(palavra))
   
                                    
    palavra_secreta_selecionada = palavra[numero]
    print(palavra[numero])
    return(palavra_secreta_selecionada)

carrega_palavra_secreta()
