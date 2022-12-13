# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('RLE.txt', 'r') as data:
    text = data.read()

def encode_rle(s):
    str_code = ''
    prev_char = ''
    count = 1
    for char in s:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code
            
str_code = encode_rle(text)
print(str_code)

with open('RLE_2.txt', 'r') as data:
    text_2 = data.read()

def decode_rle(s:str):
    count = ''
    str_decode = ''
    for char in s:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decode_rle(text_2)
print(str_decode)