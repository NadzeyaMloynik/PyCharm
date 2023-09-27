import random

while 1:
    count = input("Введите размер кортежа: ")
    if not count.isdigit():
        print("Значение введено некорректно, попробуйте снова")
    else:
        count = int(count)
        break
print("Введите диапозон значиний ")
while 1:
    a = str(input("Первое значение: "))
    try:
        a = int(a)
        break
    except:
        print("Значение введено некорректно, попробуйте снова")
while 1:
    b = str(input("Крайнее значение: "))
    try:
        b = int(b)
        break
    except:
        print("Значение введено некорректно, попробуйте снова")
if a > b:
    a, b = b, a
numbers = [random.randint(a, b) for i in range(count)]
numbers = tuple(numbers)
print(f"Сгенерированный кортеж: {numbers}")
counter = 0
for i in range(len(numbers)):
    if numbers[i] < 0:
        print(f"Индекс первого отрицательного числа: {i}")
        counter += 1
        break
if counter == 0:
    print("Отрицательные числа отсутвуют.")