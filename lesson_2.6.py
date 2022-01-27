id = 0
products = []
input_mode = True
while input_mode:
    id += 1
    name = input('Введите название товара: ')
    cost = float(input(f'Введите цену для {name}: '))
    cnt = float(input(f'Введите кол-во для {name}: '))
    unit = input(f'Введите единицу измерения для {name}: ')
    product = (id, {"название": name, "цена": cost, "количество": cnt, "eд": unit})
    products.append(product)
    input_mode = input('Ввести следующий товар (д/н): ')[0:1].upper() == 'Д'
print(products)
analytics = {
    "название": [],
    "цена": [],
    "количество": [],
    "eд": []
}
for product in products:
    for key in analytics.keys():
        analytics[key].append(product[1][key])

print(analytics)