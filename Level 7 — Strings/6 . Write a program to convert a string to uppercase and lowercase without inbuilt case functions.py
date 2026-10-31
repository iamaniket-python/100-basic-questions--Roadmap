# Write a program to convert a string to uppercase and lowercase without inbuilt case functions.

str=input("Enter a Number=")
upper=""
lower=""

for cha in str:
    if cha >= "a" and cha <="z":
        upper += chr(ord(cha)- 32)
    else:
        upper += cha

    if cha >= "A" and cha <= "Z":
        lower += chr(ord(cha) +32)
    else:
        lower +=cha

print("Uppercase",upper)
print("lower case",lower)
