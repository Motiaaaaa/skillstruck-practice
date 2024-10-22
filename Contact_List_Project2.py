answer = "y"
contact = []

while answer == "y":
    name = input ("What is their full name?")
    contact.append(name)
    answer = input("Do you want to add more contacts? Answer with y or n: ")

contact.sort()
print(contact)