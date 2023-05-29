alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
a = alfa.index('a')
e = alfa.index('e')
i = alfa.index('i')
o = alfa.index('o')
u = alfa.index('u')
palavra = input('Digite a palavra: ')
for letra in palavra:
    letra2 = letra
    if letra2 not in 'aeiou':
        posicoes = sorted([a, e, i, o, u, alfa.index(letra2)])
        if posicoes[posicoes.index(alfa.index(letra2))] - posicoes[posicoes.index(alfa.index(letra2))-1] < posicoes[posicoes.index(alfa.index(letra2))+1] - posicoes[posicoes.index(alfa.index(letra2))]:
            letra2 += alfa[posicoes[posicoes.index(alfa.index(letra2))-1]]
        elif posicoes[posicoes.index(alfa.index(letra2))] - posicoes[posicoes.index(alfa.index(letra2))-1] == posicoes[posicoes.index(alfa.index(letra2))+1] - posicoes[posicoes.index(alfa.index(letra2))]:
            if alfa[posicoes[alfa.index(letra2)-1]] < alfa[posicoes[alfa.index(letra2)+1]]:
                letra2 += alfa[posicoes[posicoes.index(alfa.index(letra2))-1]]
            else:
                letra2 += alfa[posicoes[posicoes.index(alfa.index(letra2))+1]]
        else:
            letra2 += alfa[posicoes[posicoes.index(alfa.index(letra2))+1]]
        if alfa[alfa.index(letra2[:len(letra2)-1])+2] not in 'aeiou':
            letra2 += alfa[alfa.index(letra2[:len(letra2)-1])+1]
        else:
            letra2 += alfa[alfa.index(letra2[:len(letra2)-1])+2]
    palavra = palavra.replace(letra, letra2)
    print(palavra)
print(palavra)
