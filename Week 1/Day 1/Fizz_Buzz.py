print("In THis Game If Number Is Divisible By -> 3 : Fizz\n")
print("if Number is divisible by 5 : FizzBuzz")
number = int(input("Enter a Number To Kick Start:\n"))
if number%3 == 0:
    print("FizZ")
elif number%5 == 0:
    print("FizzBuzZ")
else:
    print(number)