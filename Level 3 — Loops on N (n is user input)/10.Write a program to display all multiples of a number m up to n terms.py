# Write a program to display all multiples of a number m up to n terms

m=int(input("Enter a first number="))
n=int(input("Enter a second number="))


for i in range(1, n):
    print(m * i)
