# Write a program to read n elements into an array and print them.

n=int(input("Enter number="))

arr=[]

for i in range(n):
    element= int(input("Enter elements="))
    arr.append(element)

print("Array elements =",arr, end=" ")
