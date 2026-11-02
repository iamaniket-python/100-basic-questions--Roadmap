# Write a program to count the number of even and odd elements in an array


n = int(input("Enter number of elements = "))

arr = []

for i in range(n):
    ele = int(input("Enter the element = "))
    arr.append(ele)

count_even = 0
count_odd = 0

for elements in arr:
    if elements % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Even count =", count_even)
print("Odd count =", count_odd)