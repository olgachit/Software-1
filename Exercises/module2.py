name = input("Enter your name: ")
print("Hello", name)

import math
rds = int(input("Enter your rds: "))
area = math.pi * (rds ** 2)
print("The area of your circle is ", area)

length = float(input("Enter your length: "))
height = float(input("Enter your height: "))
Perimeter = (length * 2) + (height * 2)
area = length * height
print("The perimeter of your circle is ", Perimeter)
print("The area of your circle is ", area)

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3
print("the sum is ", sum)
print("the product is ", product)
print("the average is ", average)

talents = float(input("Enter the number of talents: "))
pounds = float(input("Enter the number of pounds: "))
lots = float(input("Enter the number of lots: "))
total_pounds = (talents * 20) + pounds
total_lots = (total_pounds * 32) + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams/1000)
remaining_grams = float(total_grams % 1000)
print(f"The mass is {kilograms} kilograms and {remaining_grams:.2f} grams.")

from random import randint, random

num1 = randint(0,9)
num2 = randint(0,9)
num3 = randint(0,9)
code = num1, num2, num3
num4 = randint(1,6)
num5 = randint(1,6)
num6 = randint(1,6)
num7 = randint(1,6)
code2 = num4, num5, num6, num7
print(code)
print(code2)
