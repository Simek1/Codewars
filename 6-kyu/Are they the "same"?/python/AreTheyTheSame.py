#1st solution

def comp(array1, array2):
    ans=False
    if array1==array2==None:
        return True
    elif array1==None or array2==None:
        return False
    elif array1==array2==[]:
        return True
    else:
        for x in array1:
            ans=False
            for k in array2:
                if x*x==k:
                    ans=True
                    array2.remove(k)
                    break
            if ans==False:
                return False
    return ans
  
#2nd solution

def comp(array1, array2):
    try:
        array2=sorted(array2)
        if sorted([x*x for x in array1])==array2:
            return True
        else:
            return False	
    except:
        return False
