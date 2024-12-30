# 1. Запись списка покупок
with open('shopping_list.txt', 'w', encoding='utf-8') as file:
    file.write('Milk\n')
    file.write('Bread\n')
    file.write('Eggs\n')

# 2. Чтение содержимого файла
with open('shopping_list.txt', 'r', encoding='utf-8') as file:
    print(file.read())

# 3. Добавление новых элементов
with open('shopping_list.txt', 'a', encoding='utf-8') as file:
    file.write('Butter\n')
    file.write('Cheese\n')

with open('shopping_list.txt', 'r', encoding='utf-8') as file:
    print(file.read())