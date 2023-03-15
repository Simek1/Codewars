def find_missing_letter(chars):
    prev=ord(chars[0])
    for x in chars[1:]:
        if prev+1!=ord(x):
            return chr(ord(x)-1)
        prev=ord(x)
