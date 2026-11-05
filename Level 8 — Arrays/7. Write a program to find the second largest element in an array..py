# Write a program to find the second largest element in an array.

n=int(input("Enter how many Number="))

arr=[]

for i in range(n):
    elements=int(input("Enter a number="))
    arr.append(elements)

largest=arr[0]
second_largest = None

for digit in arr:
    if digit > largest:
        second_largest = largest
        largest =digit

    elif digit != largest and (second_largest is None or digit > second_largest):
        second_largest =digit


if second_largest is not None:
    print("Second largest =", second_largest)
else:
    print("Second largest element does not exist")