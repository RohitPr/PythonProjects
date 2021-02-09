# Python program to calculate Body Mass Index (BMI) based on a user's weight and height.

print("Welcome to BMI Calculator")
height = float(input("\nEnter your height(in m) : "))
weight = float(input("Enter your weight(in kg) : "))

bmi = round(weight / (height ** 2), 1)

if bmi < 18.5:
    print(f"\nYour BMI is {bmi}, you are Under Weight")
elif (bmi >= 18.5) and (bmi < 25):
    print(f"\nYour BMI is {bmi}, you are Normal Weight")
elif (bmi >= 25) and (bmi < 30):
    print(f"\nYour BMI is {bmi}, you are Over Weight")
elif (bmi >= 30) and (bmi < 35):
    print(f"\nYour BMI is {bmi}, you are Obese")
else:
    print(f"\nYour BMI is {bmi}, you are Clinically Obese")
