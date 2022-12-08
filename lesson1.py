# задание 1
a = 3
b = "строка"
print(a, b)
a = int(input("Введите целое число: "))
print(a)
b = input("Введите слово: ")
print(b)
# задание 2
c = int(input("Введите время в секундах: "))
h = c//3600
m = (c-h*3600)//60
s = c-(h*3600+m*60)
print(f"{h} : {m} : {s}")
# задание 3
n = int(input("Введите целое число: "))
su = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print(f"Сумма = {su}")
# задание 4
i = int(input("Введите целое положительное число "))
max = i % 10
while i >= 1:
     i = i // 10
     if i % 10 > max:
         max = i % 10
     if i > 9:
         continue
     else:
         print(f"{max}")
         break
# задание 5
profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки = {profit / costs}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"Прибыль в расчете на одного сторудника сотавила {profit / workers:}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
# задание 6
start = int(input("Введите результат пробежки первого дня "))
finish = int(input("Введите общий желаемый результат "))
result_days = 1
result_km = start
while result_km < finish:
        start = start + 0.1 * start
        result_days += 1
        result_km = result_km + start
print(f"Вы достигнете требуемых показателей на {result_days} день")
