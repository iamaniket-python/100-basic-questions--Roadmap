# Write a program to read a number and check whether it is divisible by both 3 and 5

num=int(input("Enter a Number="))

if num % 3 == 0 and num % 5 == 0:
    print("yes it is divisible")
else:
    print("No it is not divisible")
