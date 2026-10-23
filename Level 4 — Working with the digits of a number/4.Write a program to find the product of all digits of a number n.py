# Write a program to find the product of all digits of a number n

num=input("Enter a number=")
total=1

for digit in num:
    total *= int(digit)


print(total)