# number = 1
# while number < 50:
#     print(number)
#     number += 1

# Challenge2
# my_number = int(input("Pick a number."))
# total = my_number
# while my_number != 0:
# 	my_number = int(input("Pick a number."))
# 	total += my_number 
	
# print(total)


#Challenge3
my_number = int(input("Pick a number."))
largest = my_number
while my_number != 0:
	my_number = int(input("Pick a number."))
	if my_number > largest:
		largest = my_number

print(largest)