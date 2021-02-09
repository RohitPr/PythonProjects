# Python program to split the bill among the friends.

print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? Rs "))
tip_percentage = float(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
total_people = int(input("How many people to split the bill? "))

total_price = total_bill * (1 + tip_percentage / 100)
split_money = round(total_price / total_people, 2)

print(f"Each person should pay : Rs {split_money}")
