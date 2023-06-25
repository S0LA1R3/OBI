numeros = []
for c in range(int(input())):
    numero = int(input())
    if numero == 0:
        del numeros[-1]
    else:
        numeros.append(numero)
print(sum(numeros))
