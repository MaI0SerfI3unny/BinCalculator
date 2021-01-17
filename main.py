from Type import bin
from Type import oct
from Type import hex

quess = int(input("Выбери операцию:"
                  "\n1. Перевести простое число, число в двоичную"
                  "\n2. Перевести простое число, число в шестнадцатиричную"
                  "\n3. Перевести простое число, число в восьмиричную"
                  "\n4. Дополнительно"))

def sort_bin():
    e = int(input("Сколько чисел нужно отсортировать?"))
    m=[input('Enter a number ') for x in range(e)]
    result4 = [int(item) for item in m]
    print(sorted(result4))
    what_sort=int(input("В какой код перевести: "
                        "\n\t1.Двоичный"
                        "\n\t2.Восьмеричный"
                        "\n\t3.Шестнадцатеричный"))
    if what_sort == 1:
        for item in result4:
            print(item, '=>', bin(item))
    if what_sort == 2:
        for item in result4:
            print(item, '=>', oct(item))
    if what_sort == 3:
        for item in result4:
            print(item, '=>', hex(item))


def advance():
   add = int(input("Выберете дополнительную операцию"
          "\n1.Добавления два двоичных числа"
          "\n2.Добавления два восьмеричных числа"
          "\n3.Добавления два шестнадцатеричная числа"
          "\n4.Отнимание двух двоичных числа"
          "\n5.Отнимание двух восьмеричных числа"
          "\n6.Отнимание двух шестнадцатеричных числа"
          "\n7.Отсортировать обычные числа в двоичный код"
          "\n8.Умножение двух двоичных чисел"
          "\n9.Умножение двух восьмеричных чисел"
          "\n10.Умножение двух шестнадцатеричных чисел"
          "\n11.Деление двух двоичных чисел"
          "\n12.Деление двух восьмеричных чисел"
          "\n13.Деление двух шестнадцатеричных чисел"))
   if add == 1:
      num1 = int(input("Введите первое число: "))
      num2 = int(input("Введите второе число: "))
      bin.binplus(num1, num2)
   if add == 2:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       oct.octplus(num1, num2)

   if add == 3:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       hex.hexplus(num1, num2)
   if add == 4:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       bin.binmin(num1, num2)
   if add == 5:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       oct.octmin(num1,num2)
   if add == 6:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       hex.hexmin(num1,num2)
   if add == 7:
       sort_bin()
   if add == 8:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       bin.binmn(num1, num2)
   if add == 9:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       oct.octmn(num1,num2)
   if add == 10:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       hex.hexmn(num1,num2)
   if add == 11:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       bin.bindl(num1, num2)
   if add == 12:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       oct.octdl(num1,num2)
   if add == 13:
       num1 = int(input("Введите первое число: "))
       num2 = int(input("Введите второе число: "))
       hex.hexdl(num1,num2)

def binary():
    n = int(input('Введи число которое нужно перевести в двоичную'))
    b = ''
    while n > 0:
        b = str(n % 2)+b
        n = n // 2
    while len(b) != 4:
        b = str('0' + b)
    print(b)

if quess == 1:
    binary()

elif quess == 2:
    n = int(input('Введи число которое нужно перевести в шестанадцатиричную'))
    print(hex(n))
elif quess == 3:
    n = int(input('Введи число которое нужно перевести в восьмиричную'))
    print(oct(n))
elif quess == 4:
    advance()
