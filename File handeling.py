f=open('file.txt', "r")
g=open('file.txt', "w")
# print(f)
text=f.read()
print(text) #This Does the same as the print Command
f.close()

with open('file.txt', "w"):
    g.write("My world")