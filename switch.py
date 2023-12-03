age=int(input("Input Your age: "))
match age:
    case 0 if age<18:
        print("Hi ")
    case 1 if age>=18:
        print("Hello")
    case _ :
        print("You can vote")
              