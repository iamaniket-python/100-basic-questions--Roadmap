# Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).

marks=int(input("Enter a Number="))

if marks > 90:
    print("A grade")
elif marks >= 70 :
    print("B Grade")
elif marks >= 50:
    print("C grade")
elif marks >= 30:
    print("D garde")
else:
    print("Fail")

# Enter a Number=30
# D garde