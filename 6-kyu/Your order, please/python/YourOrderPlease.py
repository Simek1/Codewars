def order(sentence):
    splited=sentence.split()
    pos=[]
    ans=["" for x in splited]
    for x in sentence:
        if x.isnumeric():
            pos.append(int(x)-1)
    j=0
    for i in pos:
        ans[i]=splited[j]
        j+=1
    ans=" ".join(ans)
    return ans
