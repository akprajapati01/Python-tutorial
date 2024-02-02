def greet():
    global age
    if(age>=18):
        print("Good morining")
    else:
        print("Good Morning Child")
    
age=(int(input("What is Your Age ?")))
greet()