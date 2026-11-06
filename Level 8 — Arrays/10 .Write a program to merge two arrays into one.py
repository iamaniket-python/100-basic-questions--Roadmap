# Write a program to merge two arrays into one

n=int(input("Enter how many number Array ="))

arr_one=[]
arr_two=[]

for i in range(n):
    elements=int(input("Enter First digit number ="))
    arr_one.append(elements)
for i in range(n):
    ele = int(input("Enter second digit Numbers="))
    arr_two.append(ele)

merge=[]

for digit in arr_one:
    merge.append(digit)

for value in arr_two:
    merge.append(value)


print("First array =", arr_one)
print("Second array =", arr_two)
print("Merged array =", merge)

