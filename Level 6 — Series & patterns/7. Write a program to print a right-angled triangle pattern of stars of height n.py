# Write a program to print a right-angled triangle pattern of stars of height n

n=int(input("ENter a Number="))



for i in range(1 ,n +1):
    for j in range(i+1):
        if i > j:
            print("*", end="")
    print()





