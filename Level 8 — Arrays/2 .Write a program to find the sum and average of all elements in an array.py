# Write a program to find the sum and average of all elements in an array

n=int(input("Enter number elements="))

arr=[]
total=0

for i in range(n):
    element= int(input("Enter element="))
    arr.append(element)
    total += element

average = total /n


print("array of sum =",arr)
print("Sum =", total)
print("Average =", average)