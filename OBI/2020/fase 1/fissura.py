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
    matrizInvertida = []
    for y in range(len(matriz[0])):
        palavra = ''
        for x in matriz:
            palavra += x[y]
        matrizInvertida.append(palavra)
    matriz.clear()

    for x in range(len(matrizInvertida)):
        palavra = ''
        for y in range(len(matrizInvertida[x])):
            if y == 0:
                palavra += matrizInvertida[x][y]
                continue
            if matrizInvertida[x][y] == '*':
                palavra += matrizInvertida[x][y]
                continue
            if matrizInvertida[x][y - 1] == '*' and int(matrizInvertida[x][y]) <= int(tamanho[1]):
                palavra += '*'
            else:
                palavra += matrizInvertida[x][y]
        matrizInvertida[x] = palavra

        for x in range(len(matrizInvertida)):
            palavra = ''
            for y in range(len(matrizInvertida[x])-1, -1, -1):
                if y == len(matrizInvertida[x])-1:
                    palavra += matrizInvertida[x][y]
                    continue
                if matrizInvertida[x][y] == '*':
                    palavra += matrizInvertida[x][y]
                    continue
                if matrizInvertida[x][y + 1] == '*' and int(matrizInvertida[x][y]) <= int(tamanho[1]):
                    palavra += '*'
                else:
                    palavra += matrizInvertida[x][y]
            matrizInvertida[x] = palavra

    for y in range(len(matrizInvertida[0])):
        palavra = ''
        for x in matrizInvertida:
            palavra += x[y]
        matriz.append(palavra)
    matrizInvertida.clear()

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
