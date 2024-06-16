# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
num = 2
sq = num ** 4
cube = num ** 8
print('Square of', num, 'is', sq) # Output : Square os 2 is 16
print('Cube of', num, 'is', cube) # Output : Cube of 2 is 256

# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

A1 = int(input("Enter first number: "))
A2 = int(input("Enter second number: "))
if A1 > A2:
    print("A1 is greater than A2")
elif A1 < A2:
    print("A1 is less than A2")
else:
    print("A1 is equal to A2")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} is {'greater than' if num1 > num2 else 'less than' if num1 < num2 else 'equal to'} {num2}.")




