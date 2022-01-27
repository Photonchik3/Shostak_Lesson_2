s = input("Введите строку: ")
words = s.split()
for i in range(len(words)):
    print(str(i + 1), words[i][0:10])