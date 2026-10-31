# Write a program to count the number of vowels and consonants in a string

str=input("Enter a number=")

vowels=0

for digit in str:
    if digit in "aeou":
        vowels = vowels + 1

print(vowels)
