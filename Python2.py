# num_of_guests = int(input("Number of Guests: "))

# NUM_PEOPLE_LG_PIZZA = 7
# NUM_PEOPLE_MED_PIZZA = 3
# NUM_PEOPLE_SM_PIZZA = 1

# large_pizzas = num_of_guests // NUM_PEOPLE_LG_PIZZA
# remaining_guests = num_of_guests % NUM_PEOPLE_LG_PIZZA

# medium_pizzas = remaining_guests // NUM_PEOPLE_MED_PIZZA
# remaining_guests = remaining_guests % NUM_PEOPLE_MED_PIZZA

# small_pizzas = remaining_guests // NUM_PEOPLE_SM_PIZZA


# print("You will need " + str(large_pizzas) + " large pizzas, " + str(medium_pizzas) + " medium pizzas, and " + str(small_pizzas) + " small pizzas.")





#Leap_Year_Calculator
# year = int(input("What year do you want to check?"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(str(year)+ " is a leap year")
#         else:
#             print(str(year) + " is not a leap year")
#     else:
#         print(str(year)+ " is a leap year")
# else:
#     print(str(year)+ " is not a leap year")






#Prime Number Calculator
# number = int(input("What number do you want to know?"))

# # print(range(number))
# factors = []
# for x in range(2, number):
#     if number % x == 0:
#         factors.append(x)

# if len(factors) > 0:
#     print(factors)
# else:
#     print(str(number) + " is a prime number")






##Factorials 
number = int(input("What number do you want to know?"))

mult_total = 1
sum_total = 0

for x in range(1, number+1):