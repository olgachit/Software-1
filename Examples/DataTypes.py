'''
#tuple
day_of_the_week=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
day_number=int(input("Enter the day number(1-7): "))
day=day_of_the_week[day_number-1]
print(f"The day {day_number} is {day}")

import random
def cast():
    first,second=random.randint(1,6),random.randint(1,6)
    return first,second
dice1,dice2=cast()
print(f"The dice shows {dice1} and {dice2}")

#set
sti=set()
print(sti)
sti.add("a")
sti.add("b")
sti.add("c")
print(sti)

#Dictionary
dt1={'Sumen':1111,'Minh':2222,'long':3333,'Hoang':4444,'Olga':5555}
name=input("Enter the name of the customer: ")
if name in dt1:
    print(f"the contact name of {name} is {dt1[name]}")
dt1['Jiya']=5555
print(dt1)
dt1['Minh']=7777
print (dt1)

dt2={"a":1,'b':2,'c':3,'a':4}
print(dt2)
del dt2['a']
print(dt2)

#tuple
tuple3=tuple(map(int,input("Enter the tuple with space between the numbers: ").split()))
print(tuple3)
print(f"maximum value is {max(tuple3)}")
print(f"minimum value is {min(tuple3)}")
'''