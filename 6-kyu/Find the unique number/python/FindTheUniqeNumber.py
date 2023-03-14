def find_uniq(arr):
    uniq=set(arr)
    if arr[0]==arr[1]:
        for x in uniq:
            if x!=arr[0]:
                return x
    else:
        for x in uniq:
            if x!=arr[3]:
                return x
