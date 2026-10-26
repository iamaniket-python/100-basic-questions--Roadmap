# Write a program to check whether a number is a perfect number.

num=int(input("Enter a number="))

total =0

for i in range(1, num):

    if num % i == 0:
        total += i

if total == num:
    print("it is perfect number")
else:
    print("not a perfect number")




