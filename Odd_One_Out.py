words = input("Type in a list of words separated by spaces.: ").split(" ")
letter_count = []
for word in words:
	if x[0] not in letter_count:
		letter_count.append(x[0])
		letter_count.append(1)
	else:
		letter_count[letter_count.index(x[0])+1] += 1