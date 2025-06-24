"""
Archion's Simple Calculator v0.01
Made by tuantechno-dev with Python 3
This program use MIT license
"""

'''
I am newbie of Python and this project is my first program of Python to test my knowleage, so code with too complex and messy :)
This program use some code from ChatGPT :)
'''

# Import libary
import sys

# Setup
lang = "en"
ver = "0.01"

# Some user-defined functions
def plus(num1, num2):
	return num1 + num2

def minus(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def devide(num1, num2):
	if num2 == 0:
		return "Sorry, cannot division by zero"
	return num1 / num2

#Welcome user
user = input("What's your username: ")
print(f"Welcome, {user}!")

while True:
	op = ""
	num1 = 0
	num2 = 0
	op = input("What operation you want (+, -, * or /)? If you want to exit this program, type 'exit': ")

	# Exit command
	if op == "exit":
		break

	# User input and check user input is the value value or not
	try:
		num1 = float(input("First number: "))
		num2 = float(input("Second number: "))
	except ValueError:
		print("Invalid input. Please enter numeric values.")
		continue

	# Other command
	print("Loading. This will take some time...")
	if op == "+":
		print("The result is:", plus(num1, num2))
	elif op == "-":
		print("The result is:", minus(num1, num2))
	elif op == "*":
		print("The result is:", multiply(num1, num2))
	elif op == "/":
		print("The result is:", divide(num1, num2))
	else:
		print("Error cannot detect a command, please type again!")

print("Stoping program, please wait...")
sys.exit()
