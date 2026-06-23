num = int(input("Enter Your NUmber:"))

for i in range(1, 11):
    if i % 2 == 0:
        continue
    elif i % 3 == 0:
        continue
    elif i % 4 == 0:
        continue
    print(i)