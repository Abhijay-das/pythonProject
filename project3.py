# bmi calculator
weight = float(input("enter your weight in kg:"))
hight  = float(input("enter your hight in cm:"))

bmi = round(weight/hight**2)
if bmi < 18.5 :
    print(f"your bmi is {bmi}and you are under weight")
elif bmi <25 :
    print(f'your bmi is {bmi} and you are perfect ')
elif bmi <30 :
    print(f'your bmi is {bmi} and you are over weight ')
else :
    print(f' your bmi is {bmi} and your are clinically obese')



