n=int(input("Input any number between 5 and 50:"))
if(n<5 or n>50):
    raise ValueError("Number is not between 5 and 50")