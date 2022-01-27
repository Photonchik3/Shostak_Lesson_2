my_list = [8, 5, 4, 4, 4]
new = int(input('Введите новый эелемент рейтинга'))
cnt = my_list.count(new)
if cnt > 1:
    my_list.insert(my_list.index(new) + cnt, new)
elif cnt == 0:
    l = len(my_list)
    for i in range(l):
        if new > my_list[i]:
            l = i
            break
    my_list.insert(l, new)

print(my_list)
