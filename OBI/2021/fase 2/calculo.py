soma = int(input())
numero1 = int(input())
numero2 = int(input())

numeros = 0
for c in range(numero1, numero2+1):
    somado = 0
    for x in list(str(c)):
        somado += int(x)
    if somado == soma:
        numeros += 1

print(numeros)
