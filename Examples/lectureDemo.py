
sum = 0
counter = 1
while counter <10:
    sum = sum + counter
    print(f"The counter, {counter}, and the sum of the counter with the sum: {sum}")
    counter = counter + 1

i= 1
n= int(input("Enter a limit"))
while i<= n:
    if i %2 == 0:
        print(f"the even number {i}")
    else:
        print(f"the odd number {i}")
    i = i+1
print("Done")

import random
n= random.randint(1,9)
number = 0
while True:
    g = int(input("Guess a number from 1 to 9: "))
    if g==n:
        print("well done")
        break
    else:
        print("try again")
        number+=1
    print(f"tried {number}")

user_input = ""
while user_input != "exit":
    user_input = input("Type something (or exit to quit): ")
    print("you typed: ", user_input)

import random
user_input = ""
while user_input != "heads":
    user_input = input("Type flip to flip the coin): ")
    if user_input == "flip":
        user_input = random.choice(["heads", "tails"])
        print("You got", user_input)

import random
result=random.choice(['heads', 'tails'])
while result != "heads":
    print("flipped:", result)
    result = random.choice(['heads', 'tails'])
    print("finally, flipped:", result)

first=0
while first<5:
    second = 1
    while second<5:
        print(f"{first} times {second} is ", first*second)
        second+=1
    first+=1
    print("all done")

i=0
while i<5:
    print(f"{i} : by while")
    i+=1

for i in range(5):
    print(f"{i} : by for")
    i+=1
