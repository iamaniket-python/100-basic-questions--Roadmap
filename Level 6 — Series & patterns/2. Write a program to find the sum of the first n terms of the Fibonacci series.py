# Write a program to find the sum of the first n terms of the Fibonacci series

n=int(input("Enter a Number="))

a=0
b=1

total=0

while n >0:
    print(a)
    total +=a

    c=a+b
    a=b
    b=c

    n-=1
print(total)