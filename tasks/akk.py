n = int(input("До какого числа считать простые числа: "))

a = [i for i in range(n)]

a[1] = 0
for m in range (2,n):
    if a[m] !=0:
        j = m * 2
        while j < n:
            a[j] = 0
            j += m
res = [i for i in a if i !=0]
print(res)