# Реализуйте RLE алгоритм: реализуйте модуль сжатия данных.

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


with open('origin_file.txt', 'r') as source:
    with open('result_file.txt', 'w') as output:
        for i in source:
            output.write(rle_encoder(i))
            print('Your encoded text was saved in result_file.txt')

#
# def rle_decoder(text):
#     result = ''
#     count = ''
#     node = False
#     for i in text:
#         if i == '"':
#             node = not node
#             continue
#         if node or not i.isdigit():
#             result += ''.join([i for _ in range((int(count) if len(count) > 0 else 1))])
#             count = ''
#             continue
#
#         count += i
#
#     return result
