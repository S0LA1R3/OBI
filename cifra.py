alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
consoante = []
for x in alfa:
    if x not in 'aeiou':
        consoante += x
a = alfa.index('a')
e = alfa.index('e')
i = alfa.index('i')
o = alfa.index('o')
u = alfa.index('u')
palavra = input('Digite a palavra: ')
c = 0
for letra in palavra:
    letra2 = letra
    posicaoLetra = alfa.index(letra)
    if letra not in 'aeiou':
        posicoes = sorted([a, e, i, o, u, posicaoLetra])
        if letra == 'z':
            letra2 += alfa[posicoes[posicoes.index(posicaoLetra) - 1]] + 'z'
        else:
            if posicaoLetra - posicoes[posicoes.index(posicaoLetra) - 1] <= posicoes[
                posicoes.index(posicaoLetra) + 1] - posicaoLetra:
                letra2 += alfa[posicoes[posicoes.index(posicaoLetra) - 1]]
            else:
                letra2 += alfa[posicoes[posicoes.index(posicaoLetra) + 1]]
            letra2 += consoante[consoante.index(letra) + 1]
        palavra = palavra.replace(palavra[c:], palavra[c:].replace(letra, letra2, 1))
    c += 1
print(palavra)
