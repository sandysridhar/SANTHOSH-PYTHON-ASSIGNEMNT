# 1. login function
def login(name):
    print("I welcome you to ",name)
    username = input("username:  ")
    password = input("password:    ")
    if username == "santo" and password == "passw":
        print("login successful")
    else:
        print("login failed")
        return login(name)
login("santhosh Raj S assignment")

# 2. odd number and even number
num= int(input("enter the number  "))
if num%2 == 0:
    print("num is even")
else:
    print("num is odd")
             


# 3. create a list of fruits and iterate through them
fruits = ["APPLE", "MANGO","ORANGE", "BANANA", "KIWI","POMEGRANATE"]
FRUIT = [x for x in fruits if "L" in x]
Tasty = [x for x in fruits  if "E" in x]
yummy = [x for x in fruits  if "O" in x]
Healthy = [x for x in fruits  if "A" in x]
print(FRUIT)
print(Tasty)
print(yummy)
print(Healthy)

