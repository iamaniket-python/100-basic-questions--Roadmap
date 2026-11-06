# Write a program to remove duplicate elements from an array

n=int(input("Enter how many number="))

arr=[]

for i in range(n):
    elements=int(input("Enter Numbers="))
    arr.append(elements)


unique=[]

for value in arr:
    if value not in unique:
        unique.append(value)

print("Original array =", arr)
print("Array without duplicates =", unique)