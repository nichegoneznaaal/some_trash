
def power(x,y):
    if x < 0 or y > 0:
        return
    else:
        res = x ** y
    print(res)

power(2,-5)

def power1(x,y):
    if x < 0 or y > 0:
        return
    else:
        while y < 0:
            lol = x
            x = x * lol
            y = y + 1
    res = 1 / x
    print(res)
power1(2, -5)