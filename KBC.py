que=["1.What is my Name ?","2.What is your Country Name ?"]
option=["a.)Rahul b.)Abhishek c.)Amit d.)Deepak","a.)India b.)Nepal c.)USA d.)Brazil"]
ans=["b.)Abhishek","a.)India"]
print("Welcome To kaun Banega Karorpati")
print("What is Your Name?")
name=input()
print("Are You Ready to start the Game?")
print("1.Yes")
print("2.No")
print("Type Above Number of Your Choice")
start=int(input())
if(start==1):
    print(que[0])
    print(option[0])
    print(que[1])
    print(option[1])
else:
    print("Thank You")
