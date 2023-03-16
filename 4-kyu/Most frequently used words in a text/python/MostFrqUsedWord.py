def top_3_words(text):
    text=text.lower()
    s_char="#/\.,:;|?!_-+="
    for x in s_char:
        text=text.replace(x," ")
    text=text.split()
    words={}
    for x in text:
        if x in words:
            words[x]+=1
        else:
            if len(x)*"'"==x:
                pass
            else:
                words[x]=1
    top1=[0,0]
    top2=[0,0]
    top3=[0,0]
    ans=[]
    keys=list(words)
    values=list(words.values())
    if values!=[]:
        top1=keys[values.index(max(values))]
        keys.remove(top1)
        values.remove(max(values))
        ans.append(top1)
    if values!=[]:
        top2=keys[values.index(max(values))]
        keys.remove(top2)
        values.remove(max(values))
        ans.append(top2)
    if values!=[]:
        top3=keys[values.index(max(values))]
        ans.append(top3)
    return ans
