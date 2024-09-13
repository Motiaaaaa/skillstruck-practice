# ride = {
#     "Miranda" : 167,
#     "Motiaa" : 155,
#     "Kim" : 86,
#     "Bob" : 76,
#     "Landen" : 101,
# }

# for x in ride.values():
#     if x >= 100:
#         print("This person is tall enough to ride.")
#     else:
#         print("This person is too short to ride.")



# dictionary = {
#   7: "first",
#   3: "second",
#   4: "third",
#   8: "fourth",
#   9: "fifth",
# }

# my_list = [int(n) for n in input().split()]
# for x in my_list:
#     if x in dictionary:
#         print("Yes")
#     else:
#         print("No")



n = int(input("How many keys in dictionary?"))

dictionary = {}
for num in range(n):
    dictionary[num] = num*num
print(dictionary)