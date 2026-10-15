# Write a program to display all odd numbers from 1 to n.

num=int(input("enter a number="))

for i in range(1 ,num +1):
    if i % 2 == 1:
        print(i,end=" ")

# enter a number=25
# 1 3 5 7 9 11 13 15 17 19 21 23 25