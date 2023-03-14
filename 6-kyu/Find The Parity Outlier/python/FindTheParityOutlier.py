def find_outlier(integers):
    ans=0
    if integers[0]%2==0 and integers[1]%2==0:
        for x in integers[2:]:
            if x%2!=0:
                ans=x
                break
    elif integers[0]%2!=0 and integers[1]%2!=0:
        for x in integers[2:]:
            if x%2==0:
                ans=x
                break
    else:
        if integers[0]%2==integers[2]%2:
            return integers[1]
        else: return integers[0]
        
    return ans
