# my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]
# rows = 5
# cols = 3

# for num in range(rows):
#     for num2 in range(cols):
#         my_list[num][num2] = my_list[num][num2] + 3

# print(my_list)



###Challenge 1 - Multiply List Values
# my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]

# mult = int(input("What do you want to multiply the list by?"))

# rows = 4
# cols = 3

# for num in range(rows):
#     for num2 in range(cols):
#         my_list[num][num2] = my_list[num][num2] * mult

# print(my_list)


###Challenge 2 - Find the Largest Value
x = int(input("What is the first number?"))

y = int(input("What is the second number?"))

z = int(input("What is the third number?"))

my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]

rows = 4
cols = 3

largest = 0

for num in range(rows):
    for num2 in range(cols):
        if my_list[num][num2] > largest:
            largest = my_list[num][num2]

print(largest)