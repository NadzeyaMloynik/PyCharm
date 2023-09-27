def division(arg1, arg2):
    try:
        div = arg1 / arg2
        return div
    except:
        return "Деление на ноль!"
    finally: print("Проверка проведена")

def int_division(arg1, arg2):
    try:
        div = arg1 // arg2
        return div
    except:
        return "Деление на ноль!"
    finally: print("Проверка проведена")

def remainder_division(arg1, arg2):
    try:
        div = arg1 % arg2
        return div
    except:
        return "Деление на ноль!"
    finally: print("Проверка проведена")

def int_num():
    while 1:
        arg = input()
        try:
            arg = int(arg)
            break
        except:
            print("Значение введено некорректно, повторите попытку.")
    return arg

print("Введите 2 числа: "
      "\nПервое число: ")
num1 = int_num()
print("Второе число: ")
num2 = int_num()
print(f"Выполнение арифметических операций: "
      f"\nСложение: {num1 + num2}"
      f"\nВычитание: {num1 - num2}"
      f"\nУмножение: {num1 * num2}"
      f"\nДеление: {division(num1, num2)}"
      f"\nЦелочисленное деление: {int_division(num1, num2)}"
      f"\nОстаток от деления: {remainder_division(num1, num2)}"
      f"\nВозведение в степень: {num1**num2}")