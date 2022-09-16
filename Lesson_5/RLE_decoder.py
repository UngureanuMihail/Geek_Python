# Реализуйте RLE алгоритм: реализуйте модуль восстановления данных.

def rle_decoder(text):
    result = ''
    count = ''
    node = False
    for i in text:
        if i == '"':
            node = not node
            continue
        if node or not i.isdigit():
            result += ''.join([i for _ in range((int(count) if len(count) > 0 else 1))])
            count = ''
            continue

        count += i

    return result


with open('origin_file.txt', 'r') as source:
    with open('result_file.txt', 'w') as output:
        for i in source:
            output.write(rle_decoder(i))
            print('Your decoded text was saved in result_file.txt')
