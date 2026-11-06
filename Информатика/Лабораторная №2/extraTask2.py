bits_str = input("Введите 7 бит: ").strip()

if len(bits_str) != 7 or any(bit not in "01" for bit in bits_str):
    print("Ошибка: нужно ввести ровно 7 символов 0 или 1.")
    exit()

bits = [int(bit) for bit in bits_str]

s1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6]
s2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6]
s3 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6]

error_position = s1 + 2 * s2 + 4 * s3

print("Синдром:", f"{s3}{s2}{s1}")

if error_position == 0:
    print("Ошибок нет.")
else:
    print("Ошибка в бите №", error_position)

    index = error_position - 1
    bits[index] ^= 1

    print("Исправленное кодовое слово:", "".join(map(str, bits)))

information_bits = [bits[2], bits[4], bits[5], bits[6]]

print("Правильное сообщение:", "".join(map(str, information_bits)))