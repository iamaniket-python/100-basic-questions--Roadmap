# Write a program to count the number of words in a sentence.

str=input("Enter a Number=")

count=1

for words in str:
    if words == " ":
        count = count + 1

print(count)
