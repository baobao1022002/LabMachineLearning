
n = int(input("n:"))
L = list()
for i in range(n):
    L.append(input(i))

print(L)
print('min: ' + min(L))
print('max: ' + max(L))

sum = 0
for i in range(n):
    sum = sum + int(L[i])
print('sum: ' + str(sum))

tam = 0
for i in range(n):
    for j in range(n):
        if (int(L[i]) < int(L[j])):
            tam = int(L[i])
            L[i] = int(L[j])
            L[j] = tam

print('sorted list:  ' + str(L))

poNumb = 0
neNumb = 0
for i in range(n):
    if (int(L[i]) > 0):
        poNumb += 1
    else:
        neNumb += 1

print('Number Positive in list: ' + str(poNumb))
print('Number Negative in list: ' + str(neNumb))