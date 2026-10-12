# Write a program to read three numbers and find the largest among them.

x=int(input("Enter a first Number="))
y=int(input("Enter a second number="))
z=int(input("Enter a third number="))

if x >= y and x > z:
    print(x,"greater number")
elif y > z and y >x:
    print(y,'greatest number')
else:
    print(z,'is greatetest')


# Enter a first Number=10
# Enter a second number=10
# Enter a third number=5
# 10 greater number
