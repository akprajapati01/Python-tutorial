n=int(input("Input any Number:"))
print(f"Multiplication Table of {n} is ")


for i in range(1,11):
    print(f"{n}*{i}","=",n*i)

try:
    for i in range(1,11):
    print(f"{n}*{i}","=",n*i)
except:
    print("Syntax Error")
