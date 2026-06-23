number = int(input("Enter a Number to Get Factorial\n"))
factorial = 1

for i in range(1, number+1):
    factorial *= i
print(factorial)