quantidadeRegistros = int(input())
registros = []

for c in range(quantidadeRegistros):
    registros.append(input())

amigos = {}
tempos = {}
for x in registros:
    if 'R' in x:
        amigos[x.split()[1]] = False
        tempos[x.split()[1]] = -2
    elif 'E' in x:
        amigos[x.split()[1]] = True
    elif 'T' in x:
        for y in amigos.keys():
            if not amigos[y]:
                tempos[y] += int(x.split()[1])
    for y in amigos.keys():
        if not amigos[y]:
            tempos[y] += 1

for x in amigos.keys():
    print(x, tempos[x])
