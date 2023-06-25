"""
Entrada                     Saída
0 -3 5 10                      10
0 -3 5 7                        7
47 50 -3 7 6 2                 57
"""

while True:
    sinalizador = {}
    somas = []
    cartoes = input().split()
    for x in cartoes:
        sinalizador[x] = 0
    for x in cartoes:
        soma = 0
        copia = []
        for z in cartoes:
            copia.append(z)
        print(copia)
        print(sinalizador)
        for y in range(int(len(cartoes)/2)):
            if sinalizador[copia[0]] < len(copia)/2:
                sinalizador[copia[0]] += 1
                print(copia[0])
                soma += int(copia.pop(0))
            else:
                sinalizador[copia[-1]] += 1
                print(copia[-1])
                soma += int(copia.pop(-1))
            if int(copia[0]) > int(copia[-1]):
                print(copia[0])
                del copia[0]
            else:
                print(copia[-1])
                del copia[-1]
        somas.append(soma)
    print(somas)
