# rows = 3
# pets = ["cat","dog","bunny","turtle","lizzard"]
# list = [[pet for pet in pets] for i in range(rows)]
# print(list)

### Multiply by the Number of Rows
# rows = int(input("How many rows do you want?"))
# mylist = [1,2,3,4,5]
# list = [[(j*rows) for j in mylist] for i in range(rows)]
# print(list)




### Weather Watcher
rows = input("Input a list of weather").split()
cols = ["windy", "breezy", "calm"]
result = []
for weather in rows:
    result2 = []
    for wind in cols:
        result2.append(weather + " " + wind)
    result.append(result2)
print(result)