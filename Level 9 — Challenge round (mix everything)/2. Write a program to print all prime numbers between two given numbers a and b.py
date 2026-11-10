# Write a program to print all prime numbers between two given numbers a and b

def check_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i ==0:
            return False

    return True

a=int(input("Enter a first Number="))
b=int(input("Enter a second Number="))

for num in range(1, b+1):
    if check_prime(num):.
        print(num,end=" ")
