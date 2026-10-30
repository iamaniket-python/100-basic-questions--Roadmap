# Write a program to print an inverted right-angled triangle pattern of stars of height n

n=int(input("Enter a Number="))

for i in range(n):
    for j in range(n -i):
            print("  *  " , end="")

    print()
