"""
==================================================================================
PROGRAM NAME: Smart Calculator
DISCREBTION: A calculator that perform conditional execution, validate user input, 
perform seven arithmetic operations, and handle errors.
==================================================================================
"""
# Menu of operations
print("----MENU OF OPERATIONS----")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Floor Division (//)")
print("6. Modulus (%)")
print("7. Exponentiation (**)")

# Accept the user choice
print()
menu_choice = input("please select an operation from the menu (1-7): ")
# Validate the user input
if menu_choice not in [ "1", "2", "3", "4", "5", "6", "7"]:
    print("Error! Invalid menu choice. Please select a valid option from the menu (1-7).")
else:
    print("you have selected option:", menu_choice)

# Accept two numbers from the user
print()
first_input = input("Enter the first number: ")
if first_input.strip() == "":
    print("Error: The input cannot be empty.")
else:
    try:
        first_number = float(first_input)
    except ValueError:
        print("Error: Please enter a valid number.")
second_input = input("Enter the second number: ")
if second_input.strip() == "":
    print("Error: The input cannot be empty.")
else:
    try:
        second_number = float(second_input)
    except ValueError:
        print("Error: Please enter a valid number.")

# check that the second number is not zero for division and modulus operations
if menu_choice in ["4", "6"] and second_input == 0:
    print("Error: Division or modulus by zero is not allowed.")
else:
    print("Both inputs are valid numbers. proceeding with the calculation.")
    exit(0)
# Using if/elif/else to route the correct operation based on the menu choice
if menu_choice == "1":
 result = first_input + second_input

elif menu_choice == "2":
 result = first_input - second_input 
 print("Result:", round(result, 2))

elif menu_choice == "3":
 result = first_input * second_input
 print("Result:", round(result, 2))

elif menu_choice == "4":
   result = first_input / second_input 
   print("Result:", round(result, 2))

elif menu_choice == "5":
   result = first_input // second_input
   print("Result:", round(result, 2))

elif menu_choice == "6":
   result = first_input % second_input 
   print("Result:", round(result, 2))

elif  menu_choice =="7":
   result = first_input ** second_input
   print("Result:", round(result, 2))

else:
   print("Error: Invalid menu choice. Please select a valid option from the menu (1-7).")