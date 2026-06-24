word = str(input("Enter a word: "))

def palindrome(word):
    if word == word[::-1]:
       print("This is a palindrome")
       return True
    else:
       print("This is not a palindrome")

palindrome()
