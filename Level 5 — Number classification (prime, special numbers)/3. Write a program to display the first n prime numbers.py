# Write a program to display the first n prime numbers

num=int(input("Enter a Number="))
count =0
candiate =2

is_prime=True

while count < num:
   is_prime= True

   for j in range(2, candiate):
       if candiate % j == 0:
           is_prime= False
           break

   if is_prime:
        print(candiate)
        count +=1

   candiate +=1




