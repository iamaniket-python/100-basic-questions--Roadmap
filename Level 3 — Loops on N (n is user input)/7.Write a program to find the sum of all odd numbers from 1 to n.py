# Write a program to find the sum of all odd numbers from 1 to n

num=int(input("Enter a number"))
odd=0

for i in range(1, num):
    if i % 2 == 1:
        odd +=i
print(odd)

# Enter a number20
# 100