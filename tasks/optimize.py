def tickets(people):
    tf = 0
    ff = 0
    for i in range(len(people)):
        if people[i] == 25:
            tf = tf + 1
        if people[i] == 50:
            if tf < 1:
                return("NO")
            else:
                tf = tf - 1
                ff = ff + 1
        if people[i] == 100:
            if tf < 3:
                if tf < 1 or ff < 1:
                    return("NO")
            if tf > 3:
                tf = tf - 3
            else:
                if ff < 1:
                    tf = tf - 3
                else:
                    tf = tf - 1
                    ff = ff - 1
    if tf < 0 or ff < 0:
        return("NO")
    return("YES")