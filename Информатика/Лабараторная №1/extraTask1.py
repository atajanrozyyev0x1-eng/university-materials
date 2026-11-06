from math import factorial

#10. Факториальная система -> десятичная
def factorial_to_decimal(number):

    result = 0
    length = len(number)

    for i, digit in enumerate(number):
        digit = int(digit)
        position = length - i
        result += digit * factorial(position)

    return result

#11. Десятичная -> система Фибоначчи
def decimal_to_fibonacci(number):

    if number == 0:
        return "0"
    fib = [1, 2]

    while fib[-1] <= number:
        fib.append(fib[-1] + fib[-2])

    if fib[-1] > number:
        fib.pop()

    result = ""
    remainder = number

    for value in reversed(fib):
        if value <= remainder:
            result += "1"
            remainder -= value
        else:
            result += "0"

    return result


#12. Десятичная -> симметричная девятиричная
def decimal_to_balanced9(number):
    
    if number == 0:
        return "0"

    digits = []

    while number != 0:
        remainder = number % 9
        number //= 9

        if remainder > 4:
            remainder -= 9
            number += 1

        digits.append(remainder)

    digits.reverse()
    result = ""

    for digit in digits:
        if digit < 0:
            result += "{^" + str(abs(digit)) + "}"
        else:
            result += str(digit)

    return result


#13. Система с основанием -10 -> десятичная
def negative10_to_decimal(number):

    result = 0
    power = 0

    for digit in reversed(number):
        result += int(digit) * ((-10) ** power)
        power += 1

    return result


while True:
    print("\nПеревод систем счисления. Вариант 15")
    print("10 - Факториальная -> десятичная")
    print("11 - Десятичная -> Фибоначчиева")
    print("12 - Десятичная -> симметричная 9-ричная")
    print("13 - Система с основанием -10 -> десятичная")
    print("0 - Выход")

    choice = input("\nВыберите операцию: ")

    if choice == "0":
        print("Программа завершена.")
        break

    elif choice == "10":
        number = input("Введите число в факториальной системе: ")
        result = factorial_to_decimal(number)

        print("Результат:", result, "(10)")

    elif choice == "11":
        number = int(input("Введите десятичное число: "))
        result = decimal_to_fibonacci(number)

        print("Результат:", result, "(Фиб)")

    elif choice == "12":
        number = int(input("Введите десятичное число: "))
        result = decimal_to_balanced9(number)

        print("Результат:", result, "(9С)")

    elif choice == "13":
        number = input("Введите число в системе с основанием -10: ")
        result = negative10_to_decimal(number)

        print("Результат:", result, "(-10)")

    else:
        print("Ошибка: выберите пункт 0 или от 10 до 13")