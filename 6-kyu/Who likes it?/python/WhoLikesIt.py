def likes(names):
    ans="no one likes this"
    if len(names)==1:
        ans=names[0]+" likes this"
    elif len(names)==2:
        ans=names[0]+" and "+names[1]+" like this"
    elif len(names)==3:
        ans=names[0]+", "+names[1]+" and "+names[2]+" like this"
    elif len(names)>3:
        ans=names[0]+", "+names[1]+" and "+str(len(names)-2)+" others like this"
    return ans
