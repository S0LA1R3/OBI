a = int(input())
b = int(input())
counter = 0
for c in range(a, b+1):
    print(c)
    for d in range(c+1):
        if d**6 == c:
            counter += 1
            break
        elif d**6 > c:
            break
print(counter)
