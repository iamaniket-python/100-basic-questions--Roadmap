# Write a program to find the product of all natural numbers from 1 to n (factorial of n)

num=int(input("Enter a number="))
fact =1

for i in range(1 , num):
    fact = fact * i

print("Factorial=",fact)

# Enter a number=20
# Factorial= 121645100408832000