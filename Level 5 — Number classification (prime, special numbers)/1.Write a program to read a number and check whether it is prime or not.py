# Write a program to read a number and check whether it is prime or not

num=int(input("Enter a Number="))
is_prime= True

if num < 2:
    is_prime =False

else:
    for i in range(2, num):
        if num % i == 0:
            is_prime =False
            break
if is_prime:
    print("it is a prime number")
else:
    print("it is not prime number")