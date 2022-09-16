# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Функция для удаления слова содержащие "абв"
def word_delete(text):
    i = 0
    while i < len(text):  # по всей длине строки выполяем
        if 'абв' in text[i]:  # если находиться абв в слове
            del text[i]  # удаляем слово целиком по индексу
            continue
        i += 1
    return text


# Чтение и добавление в фаил
with open('origin_file.txt', 'r') as source:
    with open('result_file.txt', 'w') as output:
        for i in source:
            item = str(word_delete(i.split()))
            output.write(item)
