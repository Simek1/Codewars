def productFib(prod):
    fib=[0,1,1]
    fn=0
    fn1=1
    i=0
    while fn*fn1+1<=prod:
        if i<2:
            fn=fib[i]
            fn1=fib[i+1]
        else:
            fib.append(fib[-2]+fib[-1])
            fn=fib[i]
            fn1=fib[i+1]
        i+=1
    return [fn,fn1,prod==fn*fn1]
