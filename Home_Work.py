# 1) Дано четырехзначное число. Проверить, является ли оно «счастливым билетом». Примечание: счастливым билетом называется число, в котором,
# при четном количестве цифр в числе, сумма цифр его левой половины равна сумме цифр его правой половины. Например, рассмотрим число
# 1322. Его левая половина равна 13, а правая 22, и оно является счастливым билетом(т. к. 1 + 3=2 + 2).

from unicodedata import digit


lucky_ticket = input("Input your's ticket number: ")

middle = int(len(lucky_ticket) / 2)

if len(lucky_ticket) % 2:
    print("Wrong ticket number! Must be pair number!")
else:
    lucky_ticket_right = list(map(int, lucky_ticket[:middle]))
    lucky_ticket_left = list(map(int, lucky_ticket[middle:]))
    if sum(lucky_ticket_right) == sum(lucky_ticket_left):
        print("Your's ticket is lucky :)")
    else:
        print("Your ticket isn't lucky :(")

# 2)С клавиатуры вводится шестизначное число. Проверить, является ли оно палиндромом. Примечание: палиндромом называется число, слово или
# текст, которые одинакового читаются слева направо и справа налево. Например, это числа 143341, 5555, 7117 и т. д.

print()

palindrome = input("Input your number: ")

if len(palindrome) < 1:
    print("Error. No number")
elif len(palindrome) == 1 and palindrome:
    print("Your's number is palindrome :)")
elif palindrome == palindrome[::-1]:
    print("Your", palindrome, "is palindrome")
else:
    print("Your", palindrome, "isn't palindrome")
    # 3) Есть круг с центром в начале координат и радиусом 4. Пользователь вводит с клавиатуры координаты точки x и y. Написать программу,
    # которая определит, лежит ли эта точка внутри круга или нет.

print()

x, y = float(input("x = ")), float(input("y = "))

RADIUS = 4

if abs(x) ** 2 + abs(y) ** 2 < RADIUS ** 2:
    print("Point is in circle")
else:
    print("Point is out of circle")
