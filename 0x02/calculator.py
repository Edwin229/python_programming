"""
program: command-line calculator
Description: This is a program that accept two numbers from the user and perform all seven arithmetic operations: Addition, subtraction, multiplication, division, floor division, modulus and exponentiation.
"""

# Get the two number from the user and covert them to float
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
 
# perform the basic arithmetic operation
print()
addition_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number
division_result = first_number / second_number
floor_division_result = first_number // second_number
modulus_result = first_number % second_number
exponentiation_result = first_number ** second_number

# print the result of the arithmetic operation
print("The result of addition is: ", addition_result)
print("The result of subtraction is: ", subtraction_result)
print("The result of multiplication is: ", multiplication_result)
print("The result of division is: ", division_result)
print("The result of floor division is: ", floor_division_result)
print("The result of modulus is: ", modulus_result)
print("The result of exponentiation is: ", exponentiation_result)       