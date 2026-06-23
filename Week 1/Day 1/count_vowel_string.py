word = str(input("Give a Word to Find Out Vowel in it: \n"))
vowel_count = 0

for char in word:
    if char in "aeiou":
        vowel_count += 1

print("Total Vowels: ", vowel_count)