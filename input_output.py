# some_text = open(r'C:\\Users\\р\OneDrive\\Desktop\\1.2 sample.txt.txt')
# префикс 'r' для считывания ссылки на файл
# for line in some_text:
#     print(line, end='')
# some_text.close()

# some_text = open(r'C:\\Users\\р\OneDrive\\Desktop\\1.2 sample.txt.txt')
# # префикс 'r' для считывания ссылки на файл
# for line in some_text:
#     if 'Mary' in line:
#         print(line, end='')
# some_text.close()

# with open(r'C:\\Users\\р\OneDrive\\Desktop\\1.2 sample.txt.txt') as some_text:
#     for line in some_text:
#         if 'Mary' in line:
#             print(line, end='')
# # оператор with после работы с объектом автоматически закрывает его
# with open(r'C:\\Users\\р\OneDrive\\Desktop\\1.2 sample.txt.txt') as some_text:
#     line = some_text.readline()
# читает по строке
#     while line:
#         print(line, end='')
#         line = some_text.readline()
#
# with open(r'C:\\Users\\р\OneDrive\\Desktop\\1.2 sample.txt.txt') as some_text:
#     lines = some_text.readlines()
# # вывод в виде list
# print(lines, end='')
# for line in lines[::-1]: # в обратном порядке
#     print(line, end='')


with open(r'C:\\Users\\р\OneDrive\\Desktop\\1.2 sample.txt.txt') as some_text:
    read_line = some_text.read()
# читает файл целиком
print(read_line, end='')
