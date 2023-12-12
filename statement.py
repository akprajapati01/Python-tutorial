# for i in range(11):
#     print("5","*",i,"=",5*i)
#     if(i==10):
#         break
#         print("Loop Closed")
for i in range(11):
    if(i==5):
        print("Skip The Statement")
        continue
    print("5","*",i+1,"=",5*(i+1))