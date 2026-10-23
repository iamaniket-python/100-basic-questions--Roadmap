# Write a program to count the number of even digits and odd digits in a number n.

num=input("Enter a Number=")
even=0
odd=0

for digit in num:
    if int(digit) % 2 ==0:
        even +=1
    else:
        odd +=1

print("Even digits =", even)
print("Odd digits =", odd)