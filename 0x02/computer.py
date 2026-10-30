# a file that builds a calculator in python

print("Welcome to the calculator program")
print()
number_1 = float(input("enter you first number: "))
number_2 = float(input("enter your second  number: "))
print()
choice = input(" choose operation (add/subtract: ")
print()
if choice == "add":
    result = number_1 + number_2
elif choice == "subtract":
    result = number_1 - number_2
else:
    print("invalid choice")
    result = None
print()
if result is not None:
   print(result)


