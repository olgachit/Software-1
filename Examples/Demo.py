
num1 = int(input("Enter a number: "))
num2 = float(input("Enter another number: "))
sum = num1 + num2
print(sum)

name = input("Enter your name: ")
school = input("Enter your school: ")

print("You are: ",name, " and your school name is:", school)

print(f" your name is,{name}, and your school name is:{school}")

floatVariable = 4.53476
print(f"your name is,{name}, and your float variable is,{floatVariable} ")
print(f"your name is,{name}, and your float variable is,{floatVariable:.2f} ")
'''
import math

rds = float(input("Enter RDS: "))
area = math.pi * (rds ** 2)
print(f"your RDS is,{rds}, and your area is ,{area:.2f}")
'''
intVariable = 4
floatVariable = 4.5
stringVariable = "software 1 is fun"

print(intVariable)
print(floatVariable)
print(stringVariable)

print(type(intVariable))
print(type(floatVariable))
print(type(stringVariable))

#typecasting is fun
intVariable = int(floatVariable)
print("here is the int version of floatVariable", intVariable)

shareOfLoan = 500.50/3
print(shareOfLoan)
print(int(shareOfLoan))
print(type(shareOfLoan))
