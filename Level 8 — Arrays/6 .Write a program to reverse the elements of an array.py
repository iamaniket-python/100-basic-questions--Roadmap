# Write a program to reverse the elements of an array

n=int(input("Enter a how many number="))

arr=[]

for i in range(n):
    elements=int(input("Enter a number="))
    arr.append(elements)

reverse=[]

for elements in range(n-1 ,-1, -1):
        reverse.append(arr[elements])

print("original Array=",arr)
print("reversed Array=",reverse)



