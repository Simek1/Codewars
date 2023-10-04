def calculate(expression):
    numbers=[]
    signs=[]
    number=""
    for x in expression:
        if x.isnumeric():
            number=number+x
        else:
            if x in ["+", "-", "*", "$"]:
                if number!="" or number[-1]==".":
                    numbers.append(float(number))
                    number=""
                    signs.append(x)
                else:
                    return("400: Bad request")
            elif x==".":
                number=number+"."
            else:
                return("400: Bad request")
    numbers.append(float(number))
    result=numbers[0]
    i=0
    signscp=signs.copy()
    if signs!=[]:
        for x in signscp:
            if x=="*" or x=="$":
                a=numbers.pop(i)
                b=numbers.pop(i)
                if x=="*":
                    c=a*b
                    signs.remove("*")
                else:
                    c=a/b
                    signs.remove("$")
                numbers.insert(i,c)
                i-=1
            i+=1
        result=numbers[0]
        i=0
        print(signs, numbers)
        for x in signs:
            if x=="+":
                result+=numbers[i+1]
            else:
                result-=numbers[i+1]
            i+=1
    return result
