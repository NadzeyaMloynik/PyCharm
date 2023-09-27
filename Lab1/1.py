print("Задайте диапозон")

while 1:
    a = str(input("Начальное значение: "))
    try:
        a = int(a)
        break
    except:
        print("Значение введено некорректно, попробуйте снова")
while 1:
    b = str(input("Конечное значение: "))
    try:
        b = int(b)
        break
    except:
        print("Значение введено некорректно, попробуйте снова")
if a > b:
    a, b = b, a
main_counter = 0

if b <= 1:
    print("Простые числа отсутствуют на заданном диапозоне")
else:
    if a <= 1:
        a = 2
    for i in range(a, b + 1):
        counter = 0
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                counter += 1
        if counter == 0:
            main_counter += 1
            print(f"{i} ")
    if main_counter == 0:
        print("Простые числа отсутствуют на заданном диапозоне")