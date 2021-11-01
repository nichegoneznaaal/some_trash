# y = 2x-10, если x > 0
# y = 0 , если х == 0
# y = 2 * |x\ - 1 , если x < 0
# x - целое число

x = int(input("Введите X"))

if x > 0:
    y = 2*x-10
elif x==0:
    y = 0
else:
    y = 2 * abs(x) - 1

print (f"Значение Y = {y:.3f}")