# smells = ["skunk", "lilac","rain","ocean","garbage","cleaner","cookies"]
# print(smells[0:3])
# smells[6] = "perfume"
# print(smells)
# print(len(smells))


#Challenge1
# my_list = [int(n) for n in input().split()]
# biggest = 0
# for num in my_list:
# 	if num > biggest:
# 		biggest = num

# print(biggest)



#Challenge2
my_list = [int(n) for n in input().split()]

current = my_list[0]

for num in my_list:
	if num > current:
		print(num)
	current = num