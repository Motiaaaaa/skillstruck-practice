# class Vacation:
#     def __init__ (self, place, distance, weather):
#         self.place = place
#         self.distance = distance
#         self.weather = weather
    
#     def tuesday(self):
#         print("We will be hiking on Tuesday.")
# summer = Vacation("Hawaii", 2000, "Sunny")
# summer.rating = 10
# summer.weather = "rainy"
# print(summer)
# print(summer.rating)
# print(summer.weather)


###Challenge 1
# class Friday:
#     def __init__(self, activity, friend):
#         self.activity = activity
#         self.friend = friend
#         def pictures(self):
#             print("We took so many pictures!")

# thisweekend = Friday("Movie","Charlotte")
# thisweekend.money = 20
# thisweekend.friend = "Shane"
# print(thisweekend)
# print(thisweekend.money)
# print(thisweekend.friend)


###Challenge 2
class Shopping:
    def __init__(self, item, quality):
        self.item = item
        self.quality = quality
        self.total = []
    def spending(self,cost):
        self.total.append(cost)

sportStore = Shopping("Kayak","High Quality")

sportStore.spending(300)
sportStore.spending(200)
sportStore.spending(500)

print(sportStore.total)