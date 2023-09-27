def multifunctional(arg):
    if type(arg) == list:
        minus_sum = 0
        for i in arg:
            if (type(i) == int or type(i) == float) and i < 0 :
                minus_sum += i
        print(f"Сумма отрицательных чисел списка: {minus_sum}")
        print(arg)
        arg = list(set(arg))
        print(arg)
    elif type(arg) == set:
        word_counter = 0
        for i in arg:
            if type(i) == str:
                i = i.split()
                word_counter += len(i)
        print(f"Количество слов в множестве: {word_counter}")
    elif type(arg) == int:
        counter = 0
        if arg <= 1:
            print("Число не является простым.")
        else:
            for i in range(2, arg // 2 + 1):
                if arg % i == 0:
                    counter += 1
            if counter == 0:
                print("Число является простым.")
            else:
                print("Число не является простым.")
    elif type(arg) == str:
        vowel_counter = 0
        consonant_counter = 0
        vowel_str = "аоуиеяюыэeaioyu"
        for letter in arg:
            if letter in vowel_str:
                vowel_counter += 1
            elif letter.isalpha():
                consonant_counter += 1
        arg = arg.split()
        print(f"Количество гласных: {vowel_counter}"
              f"\nКоличество согласных: {consonant_counter}"
              f"\nСамое длинное слово: {max(arg, key = len)}")
    else:
        print(f"Аргумент не соответствует ни одному из заданых типов."
              f"\nТип аргумента: {type(arg)}")

# arg = [1, -4, -9, -9 , 0, 0, 3, 2, -1, 3, 8.3, -1.2, -1.2]
# arg = {"from the inside", "livingin a drem", "still waiting", "lonely day"}
# arg = 12
# arg = 17
# arg = "wrong side of heaven"
# arg = True
arg = (1, 3, 6.7)
multifunctional(arg)