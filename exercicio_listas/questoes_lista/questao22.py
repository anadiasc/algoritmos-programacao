a = []
b = []

for i in range(2):
    a.append(input())

b.append(a)

for j in range(len(b)):
    if b[j] < 0 or b[j] != int:
        del(b[j])

print(b)
