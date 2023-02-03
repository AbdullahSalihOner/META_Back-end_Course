#input()
print("Where do you live?")
location = input()
print("So you live in " + location)

#len()
len("Hello")
print(len("Testing"))

#str()
a = 55
str(a)
print(type(a))
#int()
b = '55'
int(b)
print(type(b))
#float()
b = 55
float(b)
print(type(b))

#functions
def say_hello():
    return "Hello there !"

def say_hello(you):
    return "Hello" + you
    
