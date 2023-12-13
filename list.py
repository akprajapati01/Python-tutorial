fruits=["Apple","Mango","Pineapple","Guava","Banana","Dragonfruits","coconut",]
name=["Harry","Abhishek","Rajesh","Sonu",5,1,True]
even=[1,2,3,5,7,11]
# print(fruits)
# print(type(fruits))
# print(fruits[2])
# print(fruits[1:4])
# print(fruits[1:4:2])  #third number is jumb statement
fruits.sort()
fruits.reverse()
fruits.append("Honey")
even.sort(reverse=True)
print(fruits)
print(even)
even.insert(2,786)
print(even)
print(even.count(5))

# print(name)
# print(type(name))

# print(even)
# print(type(even))

new=fruits+name
print(new)