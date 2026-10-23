# Write a program to find the largest digit in a number n

num=input("Enter a Number=")
largest=0

for digit in num:
    if int(digit) > largest:
        largest = int(digit)
print(largest)


