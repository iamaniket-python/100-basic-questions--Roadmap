# Write a program to check whether a number n is a palindrome (reads the same reversed)

num = input("Enter a number=")

rev =num [::-1]

if num == rev:
    print("palidrome Number")
else:
    print("not a palidrome number")