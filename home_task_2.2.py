l = list(input("Введите элементы списка: "))
for i in range(len(l)-1):
    if i % 2 == 0:
        l[i], l[i + 1] = l[i + 1], l[i]
print(" ".join([str(i) for i in l]))