x=5
print(x)
def hello():
    x=3
    print(x)

hello()

def greet():
    global x
    x=10
    print(x)

greet()

print(x)