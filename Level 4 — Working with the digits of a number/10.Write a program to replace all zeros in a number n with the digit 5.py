# Write a program to replace all zeros in a number n with the digit 5

num=input("Enter a number=")

replace=""

for digit in num:
    if digit == "0":
        replace += "5"
    else:
        if digit  != "0":
            replace += digit

print(replace)