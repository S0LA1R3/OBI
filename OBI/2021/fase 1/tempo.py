quantidadeRegistros = int(input())
registros = []

for c in range(quantidadeRegistros):
    registros.append(input())

contagem = {}
for x in registros:
    tempo = 1

    if 'R' in x:
        if x.split()[1] not in contagem.keys():
            contagem[x.split()[1]] = 0
        if contagem[x.split()[1]] >= 999999:
            contagem[x.split()[1]] -= 999999

    if 'T' in x:
        tempo = int(x.split()[1])

    for y in contagem.keys():
        if not contagem[y] >= 999999 and 'R ' + y not in x:
            contagem[y] += tempo

    if 'E' in x:
        contagem[x.split()[1]] += 999999

for x in sorted(contagem.keys()):
    if contagem[x] < 999999:
        print(x, -1)
    else:
        print(x, contagem[x] - 999999)
