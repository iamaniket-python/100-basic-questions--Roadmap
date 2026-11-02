# Write a program to count the frequency of each character in a string

str=input("Enter a string=")



for words in str:
    count =0
    for char in str:
        if words == char:
            count = count +1

    print(count,end="")



