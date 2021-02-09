# Calculate the total pizza order

print("Welcome to python pizza deliveries")
size = input("Enter the size of pizza (S, M or L) : ")
bill = 0

if size == 'S':
    bill = 150
elif size == 'M':
    bill = 200
else:
    bill = 250

pepperoni = input("Do you want pepperoni for the pizza (Y or N) : ")
if pepperoni == 'Y':
    if size == 'S':
        bill += 20
    elif size == 'M' or size == 'L':
        bill += 30

extra_cheese = input("Do you want extra cheese for the pizza (Y or N) : ")
if extra_cheese == 'Y':
    bill += 20

print(f"Your final bill is Rs {bill}")
