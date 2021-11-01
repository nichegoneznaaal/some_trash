a = int(input("a = "))
b = int(input("b = "))

if b == 0:
    print ("Ошибка")
else:
    if a % b == 0:
        print (f"{a} делится на {b}")
    else:
        print (f"{a} не делится на {b}")
        print (f"остаток от деления = {a % b}")
    print (f"Частное = {a // b}")
