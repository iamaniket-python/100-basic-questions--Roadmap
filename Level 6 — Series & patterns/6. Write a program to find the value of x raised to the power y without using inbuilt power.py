# Write a program to find the value of x raised to the power y without using inbuilt power

x=int(input("Enter a first Number="))
y=int(input("Enter a second Number="))

total=1

for i in range(y):
   total *= x

print(total)
