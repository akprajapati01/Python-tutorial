def fibbo(n):
    if(n==1):
        return 0
    elif(n==1):
        return 1
    else:
        return fibbo(1)+fibbo(n-1)+fibbo(n-2)
    
print(fibbo(0))
print(fibbo(1))
print(fibbo(2))
print(fibbo(3))