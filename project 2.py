# riding roller coster checking
hight =int(input("enter your hight(in cm)"))


bill = 0
if hight >= 120:
    age = int(input("enter your age "))
    if age<12:
        print("your ticket is $5")
        bill=5
    elif age <=18:
        print("your ticket is $7")
        bill=7
    else:
        print("your ticket is $12")
        bill=12

    whant_photo = input("do you want a photo taken ? y for yes and n for no")
    if whant_photo == "y":
        bill += bill + 3
    print(f"your final bill is $ {bill}")

else:
    print('sorry you cant enter the roller coster')
    
submit.50
