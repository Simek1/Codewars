def cakes(recipe, available):
    cakes=[]
    for x in recipe:
        if x in available:
            if int(available[x]/recipe[x])!=0:
                cakes.append(int(available[x]/recipe[x]))
            else:
                return 0
        else:
            return 0
    return min(cakes)
