# Write a program to find the sum of all digits of a number n

num=input("Enter a number=")
total=0

for digit in num:
    total += int(digit)

print(total)


