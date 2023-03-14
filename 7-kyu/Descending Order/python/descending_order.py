#1st solution

def descending_order(num):
    num=str(num)
    num=sorted(num, reverse=True)
    c=''
    for x in num:
        c+=x
    c=int(c)
    return c
#2nd solution

def descending_order(num):
    num=str(num)
    num=sorted(num, reverse=True)
    num=int("".join(num))
    return num
