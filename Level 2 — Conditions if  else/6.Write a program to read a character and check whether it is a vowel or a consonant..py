# Write a program to read a character and check whether it is a vowel or a consonant.

vow=input("Enter a Name=").lower()

if vow in "aeiou":
    print(vow,"is a vowel")
else:
    print(vow, "is a consonant")