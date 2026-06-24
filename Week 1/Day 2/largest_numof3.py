n1 = int(input("Enter first number: \n"))
n2 = int(input("Enter second number: \n"))
n3 = int(input("Enter third number: \n"))

# Corrected lambda syntax using nested ternary operators
largest_num = lambda n1, n2, n3: n1 if (n1 > n2 and n1 > n3) else (n2 if n2 > n3 else n3)

print("The largest number is: ", largest_num(n1, n2, n3))