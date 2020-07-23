num1 = input("Please enter your 1st number:")
num2 = input("Please enter your 2nd number:")
num3 = input("Please enter your 3rd number:")

if (num1 > num2) and (num1 > num3):
    print ("The 1st number is the biggest!")
elif (num2 > num1) and (num2 > num3):
    print ("The 2nd number is the biggest!")
elif (num3 > num2) and (num3 > num1):
    print ("The 3rd number is the biggest!")
