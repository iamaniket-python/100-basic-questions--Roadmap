# Write a program to find the sum of all natural numbers from 1 to n.

num=int(input("Enter a number"))
natural=0

for i in range(1, num + 1):
    natural += i
    print(natural)
