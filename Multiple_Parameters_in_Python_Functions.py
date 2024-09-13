# def gifts(first, second):
#     print ("Your first choic for a birthday gift would be " + first)
#     print("Your second choice for a birthday gift would be " + second)

# gifts("bike", "basketball")
# gifts("speaker","tickets")



# choice1 = int(input("What is the first number?"))
# choice2 = int(input("What is the second number?"))

# def my_function(first, second):
# 	if first < second:
# 		print(first)
# 	else:
# 		print(second)
		

# my_function(choice1,choice2)


choice1 = int(input("What is the first number?"))
choice2 = int(input("What is the second number?"))
choice3 = int(input("What is the third number?")) 


def my_function(first, second, third):
	if first == second == third:
		print("3")
	elif first == second or second == third or first == third :
		print("2")
	else: 
		print("0")	
		
my_function(choice1,choice2,choice3)