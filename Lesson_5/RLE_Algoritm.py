# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Создание функции для сжатия данных
def rle_encoder(text):
    encoder = ''
    init_char = ''
    counter = 1

    for char in text:
        if char != init_char:
            if init_char:
                encoder += str(counter) + init_char
            counter = 1
            init_char = char
        else:
            counter += 1
    else:
        encoder += str(counter) + init_char
        return encoder
