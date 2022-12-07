# (pow(10, 2))  (pow(10, 1))   (pow(10, 0))

x = 127
print(pow(10, 2))
# 'pow' - для возведения чисел в степень
print((1 * pow(10, 2)) + 2 * (pow(10, 1)) + 7 * (pow(10, 0)))
y = 1045
print((1 * pow(10, 3)) + 0 * (pow(10, 2)) + 3 * (pow(10, 1) + 5 * pow(10, 0)))

# (pow(2, 2))  (pow(2, 1))   (pow(2, 0))

a = 0b101  # 5
print(a)
print((1 * pow(2, 2)) + 0 * (pow(2, 1)) + 1 * (pow(2, 0)))  # 5

b = 0b0110  # 6
print(b)
print((0 * pow(2, 3)) + 1 * (pow(2, 2)) + 1 * (pow(2, 1) + 0 * pow(2, 0)))  # 6

# (pow(16, 2))  (pow(16, 1))   (pow(16, 0))
z = 0x11  # 17
print(z)
print((1 * pow(16, 1)) + 1 * (pow(16, 0)))  # 17

w = 0x2cf1
print((2 * pow(16, 3) + 12 * pow(16, 2) + 15 * pow(16, 1) + 1 * pow(16, 0)))  # 11505

q = 0xffff
print((15 * pow(16, 3) + 15 * pow(16, 2) + 15 * pow(16, 1) + 15 * pow(16, 0)))  # 65535

print(format(q, '0>42b'))  # двоичная

with open('test_binary', 'bw') as test_file:
    for number in range(21):
        test_file.write(bytes([number]))
# используем встроенную функцию 'bytes' передаем число в виде списка '[]'
with open('test_binary', 'br') as test_file:
    for number in test_file:
        print(number)

with open('test_binary', 'bw') as test_file:
    test_file.write(bytes(range(21)))
with open('test_binary', 'br') as test_file:
    for number in test_file:
        print(number)