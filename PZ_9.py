# Дан словарь с произвольным количеством элементов.
# Выяснить имеется ли в нём элемент с ключом  “фрукт = яблоко” и если он отсутсвует, то добавить его в словарь.
# Вывести на экран первоначальный словарь и изменчивый.
dict = {
    "Овощ": "Огурец",
    "Ягода": "Клубника"
}
print(dict)
if "Фрукт" in dict:
    print(dict)
else:
    print("Элемент с ключом 'Фрукт' = 'Яблоко' отсутствует в словаре!")
    dict["Фрукт"] = "Яблоко"
    print(dict)
