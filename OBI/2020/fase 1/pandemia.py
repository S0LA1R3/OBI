dados = [int(n) for n in input().split()]

amigos = {}
for c in range(1, dados[0]+1):
    amigos[c] = ''

infectado = [int(n) for n in input().split()]
amigos[infectado[0]] = 'infectado'

reunioes = []
for c in range(dados[1]):
    reunioes.append(input().split())

for c in range(len(reunioes)):
    if c < infectado[1]-1:
        continue
    for x in reunioes[c]:
        if amigos[int(x)] == 'infectado':
            for y in reunioes[c]:
                amigos[int(y)] = 'infectado'
            break

infectados = list(amigos.values()).count('infectado')
print(infectados)
