def multi(c):
    result = 1
    c = c.split("\n")
    for i in c:
        i = int(i)
        result = result * i
    return(result)
