# Write a program to remove all spaces from a string

str=input("Enter a String=")
remove =""

for char in str:

    if char != " ":
        remove += char

print(remove,end="")

