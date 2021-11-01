while True:
    a = int(input("Введите 1 число: "))
    b = int(input("Введите 2 число: "))
    c = input("Введите функцию:")
    if c == '0':
        break
    elif c == '-':
        print(a-b)
    elif c == '+':
        print(a+b)
    elif c == '*':
        print(a*b)
    elif c == '/':
        if b == 0:
            print('Деление на 0 невозможно')
            break
        else:
            print(a/b)

