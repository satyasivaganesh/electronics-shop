def getMoneySpent(keyboards, drives, b):
    
    m=0
    for i in keyboards:
        for j in drives:
            if i+j>m and i+j<=b:
                m=i+j
                x=i                                           """ in hackerrank"""
                y=j
    if m==0:
        return -1
    return m
