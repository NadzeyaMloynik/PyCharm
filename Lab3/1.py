F1 = open("F1.txt", "w+")
F2 = open("F2.txt", "w+")
print("Введите информацию:\nОкончание ввода - пробел")
counter = 0
while (True):
    info = str(input("Введите строку: "))
    if info != " ":
        F1.write(info+"\n")
        if info[0] == "A":
            F2.write(info+"\n")
            counter += len(info.split())
    else:
        break
print(f"Количество слов в файле F2: {counter}")
F1.close()
F2.close()