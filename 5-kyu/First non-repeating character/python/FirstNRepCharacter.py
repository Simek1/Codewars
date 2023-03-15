def first_non_repeating_letter(string):
    s_lowered=string.lower()
    pos=[]
    counts={}
    for x in s_lowered:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    for x in counts:
        if counts[x]==1:
            pos.append(s_lowered.index(x))
    if pos==[]:
        return ''
    else:
        return string[min(pos)]
