# rows = 5
# cols = 3
# list = []
# for num in range(rows):
#     empty = []
#     for num2 in range(cols):
#         empty.append(rows)
#     list.append(empty)
# print(list)


###Secret Agent Name Generator
# first_name = ["Lena", "Kai", "Jaxon", "Sophie"]
# last_names = ["Cipher", "Voss", "Shade", "Hawke"]
# result = []
# for first in first_name:
#     sublist = []
#     for last in last_names:
#         sublist.append(first_name + last_names)
# print(result)



##Fruit Blender
rows = input("Input a list of fruits").split()
cols = ["apple", "grape", "peach", "cinnamon", "vanilla"]
list = []

for i in rows:
    col = []
    for j in cols:
        col.append(i + " " + j)
    list.append(col)
print(list)






# options = input("Input a list of fruits").split()
# boss_options = ["apple", "grape", "peach", "cinnamon", "vanilla"]
# list = []
# for fruit in options:
#     col = []
#     for fruit2 in boss_options:
#         col.append(fruit2)
#     list.append(col)
# print(list)