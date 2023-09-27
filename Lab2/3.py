import random
import numpy
def natural_num():
    while 1:
        arg = input()
        try:
            arg = int(arg)
            if arg > 0:
                break
        except:
            print("Значение введено некорректно, повторите попытку.")
    return arg
def int_num():
    while 1:
        arg = input()
        try:
            arg = int(arg)
            break
        except:
            print("Значение введено некорректно, повторите попытку.")
    return arg

print("Задайте размер матрицы:")
print("Количество строк: ")
N = natural_num()
print("Количество столбцов: ")
M = natural_num()
print("Задайте диапозон для заполнения матрицы числами: ")
print("Первая граница: ")
a = int_num()
print("Вторая граница: ")
b = int_num()
if a > b:
    a, b = b, a
s = [N, M]
s = tuple(s)
matrix = numpy.random.randint(low=a, high=b, size=s)
print(f"Изначальная матрица: {matrix}")
main_plus_counter = 0
for i in range(N):
    plus_counter = 0
    for j in range(M):
        if matrix[i][j] > 0:
            plus_counter += 1
    if plus_counter > 0:
        main_plus_counter += 1
if main_plus_counter > 0:
    for i in range(N):
        for j in range(M):
            matrix[i][j] *= -1
print(f"Изменненая матрица: {matrix}")