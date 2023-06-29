pedidos = input().split()
pequenos = int(input())
grandes = int(input())
if pequenos <= pedidos.count('1'):
  if grandes <= pedidos.count('2'):
    print('S')
  else:
    print('N')
else:
  print('N')
