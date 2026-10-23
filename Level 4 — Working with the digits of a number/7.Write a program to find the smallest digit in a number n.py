# Write a program to find the smallest digit in a number n

num=input("Enter a Number=")
smallest=int(num[0])

for digit in num:
    if int(digit) < smallest:
        smallest = int(digit)
print(smallest)

