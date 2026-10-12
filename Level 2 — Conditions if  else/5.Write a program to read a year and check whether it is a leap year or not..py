# Write a program to read a year and check whether it is a leap year or not.

x=int(input("Enter a Year="))

if x  % 400 == 0:
    print(x,"it is a leap year")
elif x % 100 ==0:
    print(x,"it is not a leap year")
elif x % 4 ==0:
    print(x,"it is leap year")
else:
    print(x,"not an leap year")

