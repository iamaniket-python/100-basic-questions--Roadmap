# Write a program to display the first n terms of the Fibonacci series

n=int(input("Enter a Number="))

a=0
b=1
c=0
while n > 0:
    print(a)

    c = a + b
    a=b
    b=c


    n-=1




