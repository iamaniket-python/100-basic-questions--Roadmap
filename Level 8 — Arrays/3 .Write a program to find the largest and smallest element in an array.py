# Write a program to find the largest and smallest element in an array

n=int(input("Enter element="))

arr=[]

for i in range(n):
    element=int(input("Enter element="))
    arr.append(element)

largest= arr[0]
smallest=arr[0]

for element in arr:
    if element > largest:
        largest = element

    if element < smallest:
        smallest = element

print("largest element=",largest)
print("smallest element=",smallest)






