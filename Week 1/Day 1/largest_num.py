num1 = int(input("Enter Number 1: \n"))
num2 = int(input("Enter Number 2: \n"))
num3 = int(input("Enter Number 3: \n"))

if num1 > num2 & num1 >num3:
    print("First Number IS Greater:", num1)
elif num2 > num1 & num2 >num3:
    print("Second Number IS Greater:", num2)
if num3 > num2 & num3 >num1:
    print("Third Number IS Greater:", num3)
else:
    print("Invalid Parameter")
