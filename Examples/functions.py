
print("hello")
def greeting():
    print("hello")
greeting()

def multiply(n):
    return n*n
n=int(input("Enter a number: "))
print(f"printing a return function", multiply(n))
cal=multiply(n)+10
print(f"the actual value {multiply(n)}, increased by 10 is {cal}")

def sum(a,b):
    return a+b
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(sum(a,b))

def multiply(a,b):
    return a*b
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(multiply(a,b))

def division(a,b):
    return a/b
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if b<=0:
    print("second number must be larger than zero")
else:
    print(division(a,b))

def subtract(a,b):
    return a-b
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(subtract(a,b))

score=[]
def square(number):
    return number*number

def append():
    while True:
        n=int(input("Enter a number: "))
        if n==0:
            break
        else:
            score.append(n)
            print(f"{n} square: ", square(n))

append()
print("Here is the list: ")
print(score)
for i in score:
    print(f"square of {i} is: {square(i)}")

list=[]

while True:
    n = int(input("Enter a number: "))
    list.append(n)
    print(list)
    largest=max(list)
    smallest=min(list)
    print(f"the largest number is {largest}")
    print(f"the smallest number is {smallest}")


numbers=[]
def calculate_sum(numbers):
    total=0
    for number in numbers:
        total+=number
    return total

def find_largest(numbers):
    for number in numbers:
        if number>largest:
            largest=number
    return largest

def find_smallest(numbers):
    for number in numbers:
        if number<smallest:
            smallest=number
    return smallest