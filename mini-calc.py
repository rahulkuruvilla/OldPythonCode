operation = input("What operation would you like? (+,-,/,*):")
num1 = float(input("What is your first number?:"))
num2 = float(input("What is your second number?:"))

if operation == ("+"):
    print(num1 + num2)
elif operation == ("-"):
    print(num1 - num2)
elif operation == ("/"):
    print(num1 / num2)
elif operation == ("*"):
    print(num1 * num2)
