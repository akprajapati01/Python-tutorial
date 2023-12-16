import time
t=time.strftime("%H:%M:%S")
hour=int(time.strftime("%H"))
print(t)
print(hour)
if(hour>0 and  hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and  hour<16):
    print("Good Afternoon Sir!")
else:
    print("Good Evening Sir!")