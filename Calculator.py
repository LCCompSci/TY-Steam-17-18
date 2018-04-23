''' TY STEAM Academy project to write a simple Calculator application
using functions '''

def addition (num1, num2):
	return num1+num2

def subtraction (num1, num2):
	return num1-num2

def multiplication (num1, num2):
	return num1*num2

def division (num1, num2):
	return num1/num2

option = 0

print ("Welcome to the Calculator")

while (option != 5):
	
	print ("\n1. Addition")
	print ("2. Subtraction")
	print ("3. Multiplication")
	print ("4. Division")
	print ("5. Exit Calculator")
	option = int(input("Select your option number: "))

	if (option != 5):
		number1 = int(input("Enter the first number: "))
		number2 = int(input("Enter the second number: "))
	
	if (option == 1):
		print ("The answer is ",addition(number1,number2))
	elif (option == 2):
		print ("The answer is ",subtraction(number1,number2))
	elif (option == 3):
		print ("The answer is ",multiplication(number1,number2))
	elif (option == 4):
		print ("The answer is ",division(number1,number2))
	elif (option == 5):
		print ("Thanks for using the Calculator! Bye!")
	else:
		print ("You didn't select a proper option!")
