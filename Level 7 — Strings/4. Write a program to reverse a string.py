# Write a program to reverse a string

str=input("Enter a String=")

reverse=""

for digit in str:
    reverse = digit + reverse

print(reverse)