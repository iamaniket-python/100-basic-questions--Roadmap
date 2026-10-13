# Write a program to read a character and check whether it is an alphabet, digit or special symbol

str=input("Enter a String=")

if str.isalpha():
    print("it is an alphabet")
elif str.isdigit():
    print("it is digit")
else:
    print("it is a speacial symbol")

# Enter a String=aniket
# it is an alphabet