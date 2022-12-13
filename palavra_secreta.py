palavras_secretas = open('palavras_secretas.txt', 'r')
palavras = []
for linha in palavras_secretas:
    linha = linha.strip()
    palavras.append(linha)

palavras_secretas.close()
