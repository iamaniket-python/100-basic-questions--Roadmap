# Write a program to display all natural numbers from 1 to n in reverse order.

rev=int(input("Enter a Number="))

for i in range(rev ,0, -1):
    print(i,end=" ")