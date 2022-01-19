#pizza order program

print("welcome to the Pizza mania ")
size = input("what size of pizza do you want? Small(s) , medium(m) , large(l)")
add_peperoni= input("do you want to add pepperoni to your pizza ? yes(y),no(n)")
extra_cheeze =  input ("do you want to add cheeze to your pizza ?yes(y),no(n)")


bill = 0
if size == "s" :
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

if add_peperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
if extra_cheeze =="y":
    bill += 1

print(f"your pizza price is ${bill}")




