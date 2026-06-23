number = int(input("Enter a Number to Get a Table of it: \n"))
for i in range(1, 11, 1):
    table = number * i
    print(f"{number} x {i} = {table}")