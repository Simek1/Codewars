def count(string):
    counts={}
    for x in string:
        if x not in counts:
            counts[x]=1
        else:
            counts[x]+=1
    return counts
