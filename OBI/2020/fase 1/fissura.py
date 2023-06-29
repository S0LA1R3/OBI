tamanho = input().split()
matriz = []

for c in range(int(tamanho[0])):
    matriz.append(input())

for x in range(len(matriz)):
    palavra = ''
    for y in range(len(matriz[x])):
        if int(matriz[x][y]) <= int(tamanho[1]):
            palavra += '*'
            nova = True
        else:
            palavra += matriz[x][y:]
            break
    matriz[x] = palavra

nova = True
while nova:
    nova = False
    matrizCagada = []
    for y in range(len(matriz[0])):
        palavra = ''
        for x in matriz:
            palavra += x[y]
        matrizCagada.append(palavra)
    matriz.clear()

    for x in range(len(matrizCagada)):
        palavra = ''
        for y in range(len(matrizCagada[x])):
            if y == 0:
                palavra += matrizCagada[x][y]
                continue
            if matrizCagada[x][y] == '*':
                palavra += matrizCagada[x][y]
                continue
            if matrizCagada[x][y - 1] == '*' and int(matrizCagada[x][y]) <= int(tamanho[1]):
                palavra += '*'
            else:
                palavra += matrizCagada[x][y]
        matrizCagada[x] = palavra

        for x in range(len(matrizCagada)):
            palavra = ''
            for y in range(len(matrizCagada[x])-1, -1, -1):
                if y == len(matrizCagada[x])-1:
                    palavra += matrizCagada[x][y]
                    continue
                if matrizCagada[x][y] == '*':
                    palavra += matrizCagada[x][y]
                    continue
                if matrizCagada[x][y + 1] == '*' and int(matrizCagada[x][y]) <= int(tamanho[1]):
                    palavra += '*'
                else:
                    palavra += matrizCagada[x][y]
            matrizCagada[x] = palavra

    for y in range(len(matrizCagada[0])):
        palavra = ''
        for x in matrizCagada:
            palavra += x[y]
        matriz.append(palavra)
    matrizCagada.clear()

    for x in range(len(matriz)):
        palavra = ''
        for y in range(len(matriz[x])):
            if y == 0:
                palavra += matriz[x][y]
                continue
            if matriz[x][y] == '*':
                palavra += matriz[x][y]
                continue
            if matriz[x][y - 1] == '*' and int(matriz[x][y]) <= int(tamanho[1]):
                palavra += '*'
            else:
                palavra += matriz[x][y]
        matriz[x] = palavra

        for x in range(len(matriz)):
            palavra = ''
            for y in range(len(matriz[x])-1, -1, -1):
                if y == len(matriz[x])-1:
                    palavra += matriz[x][y]
                    continue
                if matriz[x][y] == '*':
                    palavra += matriz[x][y]
                    continue
                if matriz[x][y + 1] == '*' and int(matriz[x][y]) <= int(tamanho[1]):
                    palavra += '*'
                else:
                    palavra += matriz[x][y]
            matriz[x] = palavra

for x in matriz:
    print(x)
