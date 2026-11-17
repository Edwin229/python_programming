# a program teaches how to write if, else, elsif command
age = 18

if age >= 18:
  print("You're eligible to vote!")
else:
  print("You're not eligible")

password = str(input("Enter your password: "))

if len(password) < 8:
  print("password is too short")
  print("please enter the string with at least 8 characters")
else: 
  print("password is valid!") 