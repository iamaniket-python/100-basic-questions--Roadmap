# Write a program to find the sum of all even numbers from 1 to n.

num=int(input("Enter a number"))
even=0

for i in range(1, num + 1):
    if i % 2 == 0:
        even += i
print(even)

# Enter a number30
# 240
