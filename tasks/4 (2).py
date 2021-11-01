numbers = "1 -2 3 1 4 -1"

##def high_and_low(numbers):
 #  num = numbers.split(" ")
 #   print(num)
 #   num2 = [int(i) for i in num]
 #   numbers1 = []
  #  ls = sorted(num2)
   # print(ls)
    #a = len(ls)
    #print(a)
    #numbers1.append(ls[0])
    #numbers1.append(ls[a - 1])
    #print(numbers1)
    #numberend = "_".join(numbers1)
    #print(numberend)

    #return

##high_and_low(numbers)

def find_next_square(sq):
    res = sq ** 0.5
    a = str(res)
    g = a.split(".")
    print(g)
    if g[1] != '0':
        return -1
    else:
        print("1")
        res1 = res + 1
        return(res1 * res1)

find_next_square(144.
)