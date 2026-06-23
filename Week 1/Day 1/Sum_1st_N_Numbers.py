number = int(input("Enter a Number: \n"))
counter = 1
total_sum = 0
while counter < number:
    total_sum += counter
    counter += 1
    
print("Sum: \n",total_sum)