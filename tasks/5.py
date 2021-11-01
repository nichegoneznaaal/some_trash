
a1 = "aoaoaoaoasdsddfrtghbvn"
a2 = "abababababa"

def sosat(a1, a2):
    res = set(a1)
    restwo = set(a2)
    normalno = res | restwo
    norm = list(normalno)
    a = (len(norm))
    i = 0
    while a > 0:
        norm[i] = ord(norm[i])
        i += 1
        a -= 1
    norm.sort()
    a = (len(norm))
    i = 0
    while a > 0:
        norm[i] = chr(norm[i])
        i += 1
        a -= 1
    end = ''.join(norm)
sosat(a1, a2)
    
def longest1(s1, s2):
    return ''.join(sorted((set(s1+s2))))

print(longest1(a1, a2))