#foods = ["spinach", "eggplant", "turkey", "broccoli"]

#for x in foods:
#    if x == "mushrooms":
#        print(x + " is gross")
#    elif x == "broccoli":
#        print(x + " is gross")
#    elif x == "fish":
#        print(x + " is gross")
#    else:
#        print(x + " is not my favorite, but it's not as bad.")



# my_list = [int(n) for n in input("Input a list of numbers that has several instances of the number 0").split()]

# counter = 0

# for x in my_list:
#     if x==0:
#         counter = counter + 1

# print(counter) 



my_list = [int(n) for n in input("Input a list of numbers.").split()]
for x in my_list:
    if x % 2==0:
        print(x,end=' ')