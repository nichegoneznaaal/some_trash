def func(a,b):
    if a > b:
        if a==b:
            return str(a)
        return str(a) + " " + str(func(a-1,b))
    else:
        if a == b:
            return str(a)
        return str(a) + " " + str(func(a+1,b))
print(func(1,200))
