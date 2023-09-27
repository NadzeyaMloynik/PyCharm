def fact (number):
    if number == 1 or number == 0:
        return 1
    else:
        return number*fact(number-1)

while 1:
    number = input(("Введите число для вычисление факториала: "))
    try:
        number = int(number)
        break
    except:
        print("Значение введено некорректно, повторите попытку.")
if number < 0:
    print("Невозможно вычисление факториала отрицательного числа")
else:
    print(f"Факториал введенного числа: {fact(number)}")