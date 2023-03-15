def in_array(array1, array2):
    ans=[]
    for sub in array1:
        for word in array2:
            if sub in word and sub not in ans:
                ans.append(sub)
                break
    return sorted(ans)
