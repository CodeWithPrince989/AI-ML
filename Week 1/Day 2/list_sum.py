numbers = list(map(int, input("Enter Numbers: ").split()))
sum = 0
# Loop up to the second-to-last element
for i in range(0, len(numbers) - 1):
    numbers[i] += numbers[i+1]
    sum = numbers[i]
    
print(sum)
