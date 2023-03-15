def solution(n):
    rom=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    dec=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    ans=""
    while n>0:
        if n>=max(dec):
            ans=ans+"M"
            n-=1000
        else:
            for i in range(len(dec)-1):
                if n>=dec[i] and n<dec[i+1]:
                    ans=ans+rom[i]
                    n-=dec[i]
    return ans
