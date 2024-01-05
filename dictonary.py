dict={1:"Abhishek",2:"Amit",3:"Deepak",4:"Alok"}
print(dict)
print(dict[1])  #gives Error when doesnt Exist
print(dict.get(2))   # does not gives Error when doesnt Exist

dict2={"Abhishek":"Civil Engineer","Alok":"Computer Science Engineer","Apple":"Fruits","Fortuner":"Car"}
print(dict2["Fortuner"])

print(dict.keys())
print(dict.values())
print(dict2.items())

for key in dict.keys():
    print(dict[key])