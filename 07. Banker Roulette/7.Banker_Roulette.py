"""
You are going to write a program which will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.
"""

import random

names_string = 'Angela, Ben, Jenny, Michael, Chloe'
names = names_string.split(", ")
names_list = list(names)

names_length = len(names_list)
result = random.randint(0, names_length - 1)

person_who_will_pay = names_list[result]
print(person_who_will_pay)
