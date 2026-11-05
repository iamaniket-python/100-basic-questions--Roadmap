# Write a program to count the frequency of each element in an array

n=int(input("Enter how many number="))

arr=[]

for i in range(n):
    elements=int(input("Enter Numbers="))
    arr.append(elements)



for words in arr:
    count = 0
    for char in arr:
        if words == char:
            count = count + 1

    print("Total count=",count)
