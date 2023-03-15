class RomanNumerals:
    @staticmethod
    def to_roman(n):
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
    @staticmethod
    def from_roman(roman_num):
        rom={"I":1,
             "V":5,
             "X":10,
             "L":50,
             "C":100,
             "D":500,
             "M":1000}
        ans=0
        skip=0
        for i in range(len(roman_num)):
            if skip==0:
                if i+1<len(roman_num):
                    if rom[roman_num[i+1]]>rom[roman_num[i]]:
                        ans+=rom[roman_num[i+1]]-rom[roman_num[i]]
                        skip=1
                    else:
                        ans+=rom[roman_num[i]]
                else:
                    ans+=rom[roman_num[i]]
            else:
                skip=0
        return ans
