# love calculator
print("welcome to the love calculator ")
name_1 = input("enter your name ")
name_2 = input("enter your partner's name ")

combined_string = name_2 + name_1
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l +o + v + e
love_score = str(true) +str( love)

if love_score<10 or love_score>90 :
    print(f"your love score is {lower_case_string}")

elif (love_score>= 40)  and  (love_score<=50) :
    print( )
