import collections
import random
import string

string = ""
while 1:
    count = str(input("Введите размер строки: "))
    if not count.isdigit():
        print("Значение введено некорректно, попробуйте снова")
    else:
        count = int(count)
        break
for i in range(0, count):
    string += str(random.randint(0,9))
print(f"Сгенерированная строка: {string}")
numbers_in_string = collections.Counter(string)
print(numbers_in_string)