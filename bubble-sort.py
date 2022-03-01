
L = [8, 7, 6, 5, 4, 9, 312, 23]
print(L)


for i in range(len(L) - 1):
    for j in range(0, len(L) - i - 1):
        if L[j] > L[j + 1]:
            L[j], L[j+1], = L[j+1], L[j]


print(L)
