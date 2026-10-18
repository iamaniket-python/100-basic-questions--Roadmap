# Write a program to count the number of digits in a number n

n=int(input("Enter a Number="))
count=0

if n == 0:
    count =1
else:
    n = abs(n)

    while n > 0:
        count +=1
        n = n // 10

print("Total count=",count)