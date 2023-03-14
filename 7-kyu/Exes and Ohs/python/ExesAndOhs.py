def xo(s):
    x=0
    o=0
    for k in s.lower():
        if k=="x":
            x+=1
        elif k=="o":
            o+=1
    if x==o:
        return True
    else: return False
