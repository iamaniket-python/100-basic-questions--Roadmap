# Write a program to check whether a number is an Armstrong number

num= int(input("Enter a Number="))
original = num
count = 0

while num > 0:
    digit = num % 10
    count += digit ** 3
    num //= 10

if count == original:
    print("It is armstrong number")
else:
    print("not an armstrong")




