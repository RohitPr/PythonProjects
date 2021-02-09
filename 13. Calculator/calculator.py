from art import logo
print(logo)
calculate = True

while calculate:
    num1 = float(input("What is the first number ? : "))
    operation = input('+\n-\n*\n/\nPick an operation : ')
    num2 = float(input("What's the next number? : "))

    def add(num1, num2):
        return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    def mul(num1, num2):
        return num1 * num2

    def div(num1, num2):
        return num1 / num2

    if operation == '+':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == '-':
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif operation == '*':
        print(f"{num1} * {num2} = {mul(num1, num2)}")
    elif operation == '/':
        print(f"{num1} / {num2} = {div(num1, num2)}")
    else:
        print("Wrong Choice")

    continue_calculation = input(
        "Type 'y' for new calculation and Type 'n' for exiting the calculator : ")
    if continue_calculation == 'n':
        calculate = False
        print("Goodbye")
