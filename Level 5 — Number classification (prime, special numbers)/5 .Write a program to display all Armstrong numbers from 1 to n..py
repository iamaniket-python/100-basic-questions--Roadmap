# Write a program to display all Armstrong numbers from 1 to n.


n = int(input("Enter a number: "))

for num in range(1, n + 1):
    original = num
    temp = num
    count = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        count += digit ** digits
        temp //= 10

    if count == original:
        print(original)





