def dig_pow(n, p):
    r=str(n)
    sqr=0
    for x in r:
        sqr+=int(x)**p
        p+=1
    k=1
    while k*n<sqr+1:
        if k*n==sqr:
            return k
        k+=1
    return -1
