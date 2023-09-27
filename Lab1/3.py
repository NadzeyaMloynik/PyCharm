import collections

print("Введите список чисел: ")
number_list = []
while 1:
    is_continue = str(input("Ввод числа в список: "
          "\n Да - 1"
          "\n Нет - любой символ\n"))
    if is_continue == "1":
        while 1:
            temp = str(input("Введите число: "))
            try:
                temp = int(temp)
                number_list.append(temp)
                break
            except:
                print("Значение введено некорректно, попробуйте снова")
    else:
        break

counter = 0

print(number_list)
numbers_in_list = collections.Counter(number_list)
number_list = list(set(number_list))
print(numbers_in_list)
for i in range(0, len(number_list)):
    counter += numbers_in_list[number_list[i]] // 2
print(f"Количество пар в списке чисел: {counter}")