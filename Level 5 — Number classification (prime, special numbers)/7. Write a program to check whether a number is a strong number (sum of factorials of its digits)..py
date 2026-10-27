# Write a program to check whether a number is a strong number (sum of factorials of its digits).

num=int(input("Enter a number="))

original =num

total =0

while num > 0:
    fact =1
    digit = num % 10
    num = num // 10

    for i in range(1, digit +1):
        fact *= i

    total += fact


if total == original:
    print("it is strong number")
else:
    print("not an strong number")



