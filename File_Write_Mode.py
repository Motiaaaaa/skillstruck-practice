# file = open("example.txt", "w")
# file.write("In short, I love to code!")
# file.close()

# file = open("porcupine.txt","w")




##Never Mind
# file = open("email.txt","w")
# file.write("Never mind")
# file.close()



##Custom Greeting Cards
answer = input("What do you want to replace the text with?")
file = open("report.txt", "w")
file.write(answer)
file.close()

file = open("report.txt", "r")
print(file.read())
