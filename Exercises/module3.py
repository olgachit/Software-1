#1
length = float(input("Enter the length of Zander in centimeters: "))
if length<42:
    remaining = 42-length
    print(f"Release the fish back into the lake, your fish is {remaining} centimeters below the size limit.")
else:
    print("size is within size threshold")

#2
cabin_class = input("Enter the cabin class: ")
if cabin_class=="LUX":
    print("LUX: upper-deck cabin with a balcony")
elif cabin_class=="A":
    print("A: above the car deck equipped with a window")
elif cabin_class=="B":
    print("B: windowless cabin above the car deck")
elif cabin_class=="C":
    print("C: windowless cabin below the car deck")
else:
    print("Invalid cabin class")

#3
gen=str(input("Enter your gender: "))
hemo=int(input("Enter your hemoglobin: "))
if gen=="female":
    if hemo<117:
        print("Your hemoglobin is low")
    elif 117<=hemo<=155:
        print("Your hemoglobin is normal")
    else:
        print("Your hemoglobin is high")
if gen=="male":
    if hemo<134:
        print("Your hemoglobin is low")
    if 134<=hemo<=167:
        print("Your hemoglobin is normal")
    else:
        print("Your hemoglobin is high")

#4
year=int(input("Enter a year: "))
if (year%4==0) or (year%100==0 and year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
