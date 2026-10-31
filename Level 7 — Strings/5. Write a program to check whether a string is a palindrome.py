# Write a program to check whether a string is a palindrome

str= input("Enter a String=")

reverse =""

for text in str:
    reverse = text + reverse


if str ==  reverse:
    print("it is palidrome")
else:
    print("not plaidrome")



