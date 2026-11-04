# Write a program to search for an element in an array (linear search).

n = int(input("Enter number of elements = "))

arr = []

for i in range(n):
    element = int(input("Enter element = "))
    arr.append(element)

target = int(input("Enter element to search = "))

found = False

for element in arr:
    if element == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")