# Write a program to read three numbers and find the smallest among them

x=int(input("Enter a first Number="))
y=int(input("Enter a second number="))
z=int(input("Enter a third number="))

if x <= y and x < z:
    print(x,"smallest number")
elif y < z and y < x:
    print(y,'smallest number')
else:
    print(z,'is smallest')

# Enter a first Number=65
# Enter a second number=65
# Enter a third number=23
# 23 is smallest
