chocolates = []
for c in range(int(input())):
    chocolates.append(int(input()))
chocolates.sort(reverse=True)

preco = 0
for c in range(0, len(chocolates) - len(chocolates) % 3, 3):
    if c == len(chocolates) - len(chocolates) % 3:
        break
    preco += sum(chocolates[c:c + 2])

del chocolates[:len(chocolates) - len(chocolates) % 3]
preco += sum(chocolates)
print(preco)
