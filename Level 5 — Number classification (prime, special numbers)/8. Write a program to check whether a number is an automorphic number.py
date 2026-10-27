# Write a program to check whether a number is an automorphic number

num =int(input("Enter a number="))
original = num

square=1

for i in range(2):
    square *=original
    
digits =len(str(original))

if square % (10 ** digits) ==  original:
    print("it is an Automorphic")
else:
    print("it is not an Automorphic number")


