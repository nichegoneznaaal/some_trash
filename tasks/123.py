def zero(*args):
    a = 0
    if len(args) == 0:
        return a
    else:
        if args[0][1] == '+':
            return(a + args[0][0])
        if args[0][1] == '-':
            return(a - args[0][0])
        if args[0][1] == '*':
            return(a * args[0][0])
        if args[0][1] == '/':
            return(a // args[0][0]) 
def one(*args):
    a = 1
    if len(args) == 0:
        return a
    else:
        if args[0][1] == '+':
            return(a + args[0][0])
        if args[0][1] == '-':
            return(a - args[0][0])
        if args[0][1] == '*':
            return(a * args[0][0])
        if args[0][1] == '/':
            return(a // args[0][0])
def two(*args):
    a = 2
    if len(args) == 0:
        return a
    else:
        if args[0][1] == '+':
            return(a + args[0][0])
        if args[0][1] == '-':
            return(a - args[0][0])
        if args[0][1] == '*':
            return(a * args[0][0])
        if args[0][1] == '/':
            return(a // args[0][0])
def three(*args):
    a = 3
    if len(args) == 0:
        return a
    else:
        if args[0][1] == '+':
            return(a + args[0][0])
        if args[0][1] == '-':
            return(a - args[0][0])
        if args[0][1] == '*':
            return(a * args[0][0])
        if args[0][1] == '/':
            return(a // args[0][0])
def four(*args):
    a = 4
    if len(args) == 0:
        return a
    else:
        if args[0][1] == '+':
            return(a + args[0][0])
        if args[0][1] == '-':
            return(a - args[0][0])
        if args[0][1] == '*':
            return(a * args[0][0])
        if args[0][1] == '/':
            return(a // args[0][0])
def five(*args):
    a = 5
    if len(args) == 0:
        return 5
    else:
        if args[0][1] == '+':
            return(a + args[0][0])
        if args[0][1] == '-':
            return(a - args[0][0])
        if args[0][1] == '*':
            return(a * args[0][0])
        if args[0][1] == '/':
            return(a // args[0][0])
def six(*args):
    a = 6
    if len(args) == 0:
        return a
    else:
        if args[0][1] == '+':
            return(a + args[0][0])
        if args[0][1] == '-':
            return(a - args[0][0])
        if args[0][1] == '*':
            return(a * args[0][0])
        if args[0][1] == '/':
            return(a // args[0][0])
def seven(*args):
    a = 7
    if len(args) == 0:
        return a
    else:
        if args[0][1] == '+':
            return(a + args[0][0])
        if args[0][1] == '-':
            return(a - args[0][0])
        if args[0][1] == '*':
            return(a * args[0][0])
        if args[0][1] == '/':
            return(a // args[0][0])
def eight(*args):
    a = 8
    if len(args) == 0:
        return a
    else:
        if args[0][1] == '+':
            return(a + args[0][0])
        if args[0][1] == '-':
            return(a - args[0][0])
        if args[0][1] == '*':
            return(a * args[0][0])
        if args[0][1] == '/':
            return(a // args[0][0])
def nine(*args):
    a = 9
    if len(args) == 0:
        return a
    else:
        if args[0][1] == '+':
            return(a + args[0][0])
        if args[0][1] == '-':
            return(a - args[0][0])
        if args[0][1] == '*':
            return(a * args[0][0])
        if args[0][1] == '/':
            return(a // args[0][0])

def plus(a):
    m = [a, '+']
    return m
def minus(a):
    m = [a, '-']
    return m
def times(a):
    m = [a,'*']
    return m
def divided_by(a):
    m = [a, '/']
    return m







import string

def is_pangram(s):
    s = s.lower()
    a = set(s)
    a = list(a)
    for i in a:
        if (i == ' ') or (i == '!') or (i == '?') or (i == '-'):
            a.remove(i)
    a = ''.join(sorted(a))
    b = string.ascii_lowercase
    if a == b:
        return True
    else:
        return False