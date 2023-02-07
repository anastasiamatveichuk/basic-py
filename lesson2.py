# exercise 1
list = [3, "t", 67.3, True, complex (5, 6)]
for i in list:
    print(f'{i} is {type(i)}')
# exercise 2
list_a = input("Введите элементы списка ").split()
i = 0
if len(list_a) % 2 == 0:
    while i < len(list_a):
        el = list_a[i]
        list_a[i] = list_a[i + 1]
        list_a[i + 1] = el
        i += 2
else:
    while i < len(list_a) - 1:
        el = list_a[i]
        list_a[i] = list_a[i + 1]
        list_a[i + 1] = el
        i += 2
print(list_a)
# exercise 4
str = input("Введите строку ")
word = str.split(' ')
for i, el in enumerate(word, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")
# exercise 5
my_list = [6, 5, 4, 3, 2, 1]
print(f"Рейтинг - {my_list}")
number = int(input("Введите число "))
c = my_list.count(number)
for el in my_list:
    if c > 0:
        i = my_list.index(number)
        my_list.insert(i+c, number)
        break
else:
    if number > el:
        my_list.insert(my_list.index(el), number)
    elif number < my_list[len(my_list) - 1]:
        my_list.append(number)
print(my_list)
# exercise 3
num = input("Введите число от 1 до 12 ")
list_season = ["зима", "весна", "лето", "осень"]
if num == 12 or num <= 2:
    print(list_season.pop(0))
elif num >= 3 or num <= 5:
    print(list_season.pop(1))
elif num >= 6 or num <= 8:
    print(list_season.pop(2))
else:
    print(list_season.pop(3))
