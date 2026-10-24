# Write a program to display all prime numbers from 1 to n

num=int(input("Enter a Number="))

is_prime=True

if num < 2:
    is_prime=False
else:
    for n in range(2, num + 1):
        is_prime =True

        for j in range(2, n):
            if n % j == 0:
                is_prime=False
                break
        if is_prime:
          print(n)
