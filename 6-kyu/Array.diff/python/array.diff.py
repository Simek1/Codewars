def array_diff(a, b):
    for x in b:
        while x in a:
            a.remove(x)
    return(a)
