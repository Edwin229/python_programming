"""
============================================================================
PROGRAM NAME: Robust Calculator
DISCREPTION: A typre-aware calculator that validate user input,
performs seven arithmetic operations, handles errors, and summarizes results.
=============================================================================
"""

# collect two numbers from the user
first_input = input("Enter the first_number: ")
second_input = input("Enter the second_number: ")

# Displaying the data types before casting
print()
print("----DATA TYPE BEFORE CASTING----")
print("first input type:", type(first_input))
print("second input type:", type(second_input))

# convert the two input to float and handle invalid entries
print()
first_number = float(first_input)
second_number = float(second_input)

# Use isinstances to check the numeric value
if isinstance(first_number, (int,float)) and isinstance(second_number, (int,float)):

    # Displaying the data type after casting
    print("----DATA TYPE AFTER CASTING----")
    print("first input:", type(first_number))
    print("second input:", type(second_number))

# store result hear
print()
results_list = []
# Arithmetic operation 
print("----ARITHMETIC OPERATION---")

# Addtion
addition = first_number + second_number
results_list.append(addition)
print("Addition:", round(addition, 2))

# Subtraction
substraction = first_number - second_number
results_list.append(substraction)
print("Subtraction:", round(substraction, 2))

# Multiplication
multiplication = first_number * second_number
results_list.append(multiplication)
print("Multiplication:", round(multiplication, 2))

# Division
if second_number != 0:
    division = first_number / second_number
    results_list.append(division)
    print("Division:", round(division, 2))
else:
    print("Division: Error! cannot divide by zero.")

# Floor divistion
if second_number != 0:
 floor_divistion = first_number // second_number
 results_list.append(floor_divistion)
 print("Floor Division:", round(floor_divistion, 2))
else:
    print("Floor division: Error! cannot divide by zero.")
# Modulus
if second_number != 0:
 modulus = first_number % second_number
 results_list.append(modulus)
 print("Modulus:", round(modulus, 2))
else:
    print("Modulus: Error! cannot divide by zero.")
# Exponentiation
try:
 exponentiation = first_number ** second_number
 results_list.append(exponentiation)
 print("Exponentiation:", round(exponentiation, 2))

except OverflowError:
 print("Exponencial: result is too large!")

# Display the summery
print()
print("----SUMMARY CALCULATION----")
print("Total valid results:", len(results_list))
print("Sum of the results:", round(sum(results_list), 2))
print("Maximum results:", round(max(results_list), 2))
print("Minimum results:", round(min(results_list), 2))