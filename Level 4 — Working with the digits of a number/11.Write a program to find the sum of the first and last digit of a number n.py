# Write a program to find the sum of the first and last digit of a number n

num=int(input("Enter a Number ="))

last = num % 10

while num >=10:
    num = num //10

first =num

total =first + last

print(total)

