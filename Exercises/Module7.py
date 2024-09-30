
#1
seasons=("spring","summer","autumn","winter")
month_number=int(input("Enter a month number: "))
if month_number<1 or month_number>12:
    print("Invalid month number")
else:
    season=seasons[(month_number-1)//3]
    print(f"The season of month {month_number} is {season}")

#2
names=set()
while True:
    name=input("Enter a name: ")
    if name=="":
        break
    if name in names:
        print("Existing name")
    else:
        names.add(name)
        print("New name")
print("Input names:")
for name in names:
    print(name)

#3
airports={}
while True:
    choice=input("Enter 'new' to create a new airport: ")
    if choice=="new":
        icao_code=input("Enter icao code: ")
        name=input("Enter airport name: ")
        airports[icao_code]=name
        print("Created new airport")
    elif choice=="fetch":
        icao_code=input("Enter icao code: ")
        if icao_code in airports:
            print("The name of the airport is", airports[icao_code])
        else:
            print("Airport not found")
    elif choice=="exit":
        break

airports=dict()
choice=input("Enter 'new' to create a new airport: ")
while True:
    if choice=="new":
        icao_code=input("Enter icao code: ")
        name=input("Enter airport name: ")
        airports[icao_code]=name
        print("Created new airport")
    elif choice=="fetch":
        icao_code=input("Enter icao code: ")
        if icao_code in airports:
            print("The name of the airport is", airports[icao_code])
        else:
            print("Airport not found")
    elif choice=="exit":
        break

