print("Welcome to Marraige calculator")
age=int(input("Input your age:"))
print("1.Male")
print("2.Female")
gender=int(input("Please write number before your gender:"))
if(gender==1):
    if(age>=21):
        print("You can marry")
    else:
        print("You cannot marry")
else:
    if(age>=18):
        print("You can marry")
    else:
        print("You cannot marry")
