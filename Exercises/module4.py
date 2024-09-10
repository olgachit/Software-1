
#1
counter=1
while counter <= 1000:
    if counter%3==0:
       print(counter)
    counter+=1

#2
user_input=float(input("Enter your number in inches: "))
while user_input != (user_input<0):
    print(f"{user_input} in centimeters is, {user_input*2.54}")
    user_input=float(input("Enter your number in inches: "))
    break

#3
smallest= None
largest= None
while True:
    numstring=input("Enter a number: ")
    if numstring=="":
        break
    num=int(numstring)
    if smallest is None or largest is None:
        smallest=num
        largest=num
    else:
        if num<smallest:
            smallest=num
        if num>largest:
            largest=num
    print(f"{smallest} and {largest}")

smallest= None
largest= None
while True:
    user_input=(input("Enter a number: "))
    if user_input=="":
        break
    number=float(user_input)
    if largest is None or number>largest:
        largest=number
    if smallest is None or number<smallest:
        smallest=number
print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")

#4
import random
random=random.randint(1,10)
while True:
    number=int(input("Enter a number from 1 to 10: "))
    if number>random:
        print("Too high")
    else:
        print("Too low")
    if number==random:
            print("Correct")

#5
username="python"
password="rules"
name=""
word=""
counter=0
while name!=username and word!=password:
    name=input("Enter your username: ")
    word=input("Enter your password: ")
    counter+=1
    if counter==5:
      print("Access denied")
      break
    print("wellcome")

tries=0
while tries<5:
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    if username=="python" and password=="rules":
        print("Welcome")
        break
    tries+=1
print("Access denied")

#6
import random
points=int(input("How many points do you want? "))
inCircle=0
counter=0
while counter<points:
    xOfPoint=float(random.uniform(-1,1))
    yOfPoint=float(random.uniform(-1,1))

