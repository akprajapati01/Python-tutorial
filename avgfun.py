def avg (a,b,c):
    av=(a+b+c)/3
    return av

d=avg(5,8,1)
print(d)

def avg1(a,b,c=1):
    av=(a+b+c)/3
    print(av)

avg1(5,9)    

def avg2(a=4,b=7,c=87):
    av=(a+b+c)/3
    print(av)

avg2()

def avg2(a=4,b=7,c=87):
    av=(a+b+c)/3
    print(av)

avg2(1,6,2)