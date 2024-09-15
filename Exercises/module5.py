#1
import random

num_dice = int(input("Enter the number of dice: "))
total_sum = 0
list=[]
for i in range(num_dice):
    roll = random.randint(1, 6)
    list.append(roll)
    total_sum += roll
print(list)
print(f"The sum of all dice rolls is: {total_sum}")

#2
numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    else:
        number = float(user_input)
        numbers.append(number)
numbers.sort(reverse=True)
top_five = numbers[:5]
print("The five greatest numbers are:", top_five)

#3
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        user_input = int(user_input)
        is_prime = True

    if user_input <=1:
        print("The number is not a prime number")
        is_prime = False
    else:
        for i in range(2, int(user_input**0.5)+1):
            if user_input % i == 0:
                is_prime = False
                break
    if is_prime==True:
        print("The number is a prime number")
    else:
        print("The number is not a prime number")
#4
cities = []
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)
print("The cities you entered are:")
for city in cities:
    print(city)
