# Write a program to check whether a number is prime, using a function/method

def check_prime(num):

    if num <=1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False


    return True


n= int(input("Enter a number="))

if check_prime(n):
    print("prime Number")
else:
    print("not a prime number")