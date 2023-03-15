#1st solution

def high(x):
    alhp=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    points=[]
    x=x.split()
    for e in x:
        p=0
        for l in e:
            p+=(alhp.index(l)+1)
        points.append(p)
    return x[points.index(max(points))]
  
#2nd soluton
  
  def high(x):
    points=[]
    x=x.split()
    for word in x:
        points.append(sum([ord(e)-96 for e in word]))
    return x[points.index(max(points))]
