#who will pay the bill
#way 1
import random
names_string = input("give me everybodys name, seperated by a comma.")
names = names_string.split(",")
number_names = len(names)
rando_choice = random.randint(0 , number_names-1)

person_who_will_pay = names[rando_choice]
print(person_who_will_pay + " is going to pay the bill ")

#way2

random_choice_var = random.randint(0 , number_names-1)
person_who_will_pay = names[random_choice_var]
print(person_who_will_pay)

