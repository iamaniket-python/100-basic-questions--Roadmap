# Write a program to read the marks of 5 subjects and print the total and average


marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))
marks4 = float(input("Enter marks of subject 4: "))
marks5 = float(input("Enter marks of subject 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
average = total / 5

print("Total marks:", total)
print("Average marks:", average)

# Enter marks of subject 1: 87
# Enter marks of subject 2: 85
# Enter marks of subject 3: 90
# Enter marks of subject 4: 76
# Enter marks of subject 5: 98
# Total marks: 436.0
# Average marks: 87.2
