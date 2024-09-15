#1
'''
import random

def dice():
    roll=random.randint(1,6)
    while roll!=6:
        print(roll)
        roll=random.randint(1,6)
    print(roll)
    return roll
dice()

#2
import random
def dice():
    max_sides=int(input("How many sides do you want?"))
    roll=random.randint(1,max_sides)
    while roll!=max_sides:
        print(roll)
        roll=random.randint(1,max_sides)
    print(roll)
    return roll
dice()

#3
gallons=""
def conversion():
    return gallons*3.785
while True:
    gallons=float(input("Enter volume in gallons: "))
    if gallons>0:
        print(conversion())
    else:
        break
'''
#4
n=[]
def listSum(n):
    total=0
    for number in n:
        total+=number
    return total
while True:
    number=int(input("Enter a number: "))
    if number!="":
       n.append(number)
    break
result=listSum(n)
print(result)

#5
def evenList(n):
    evenList=[]
    for number in n:
        if number%2==0:
            evenList.append(number)
    return evenList
result=evenList(n)
print(f"even list: {result}")

#6
import math
def pizza(diameter,price):
    radius=(diameter/2)/100
    area=math.pi*radius*radius
    unitPrice=price/area
    return unitPrice

a_diameter=int(input("Enter the diameter of the pizza: "))
a_price=int(input("Enter the price of the pizza: "))
b_diameter=int(input("Enter the diameter of the pizza: "))
b_price=int(input("Enter the price of the pizza: "))

