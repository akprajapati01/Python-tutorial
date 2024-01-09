try:
    list=[1,2,6,3,2,5,4]
    i=int(input("Input Any Index of the list:"))
    print(list[i])
except:
    print("Out of Range")
finally:
    print("I am Always Executed")


def function():
    try:
        list=[1,2,6,3,2,5,4]
        i=int(input("Input Any Index of the list:"))
        print(list[i])
        return 5
    except:
        print("Out of Range")
        return 7
    finally:
        print("I am Always Executed")
        return 9

x=function()
print(x)