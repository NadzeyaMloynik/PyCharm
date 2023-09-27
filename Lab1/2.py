message = str(input("Введите текст: "))
vowel_counter = 0
consonant_counter = 0
word_counter = 0
vowel_str = "аоуиеяюыэeaioyu"
for letter in message:
    if letter in vowel_str:
        vowel_counter += 1
    elif letter.isalpha():
        consonant_counter += 1
word_counter = len(message.split())
print(f"Количество гласных букв: {vowel_counter}\nКоличество согласных букв: {consonant_counter}\nКоличество слов в строке: {word_counter}")

