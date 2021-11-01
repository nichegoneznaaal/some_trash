name = "da ho"

def abbrev_name(name):
    end = []
    a = name.split(" ")
    fn = " ".join(a[0])
    fn = fn.split(" ")
    end.append(fn[0])
    end.insert(1, ".")
    fn = " ".join(a[1])
    fn = fn.split(" ")
    end.append(fn[0])
    end1 = "".join(end)
    print(end1)
    end2 = end1.upper()
    print(end2)
    return

abbrev_name(name)