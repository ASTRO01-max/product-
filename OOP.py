# class Car:
#     def __init__(self, name, brend, year):
#         self.name = name
#         self.brend = brend
#         self.year = year

#     def car_info(self):
#          print(f"Mashina nomi: {self.name}, brend: {self.brend}, Yili: {self.year}")

# car = Car("Tesla X", "Tesla", 2020) 
# car.car_info()
""""""

# N = input("Rim raqamlarni kiriting: ").strip()
# ans = 0

# rim_num = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }

# for i in range(len(N)):
#     if i + 1 < len(N) and rim_num[N[i]] < rim_num[N[i + 1]]:
#         ans -= rim_num[N[i]]
#     else:
#         ans += rim_num[N[i]]

# print(ans)
""""""

# class Solution:
#     @staticmethod
#     def rim_to_arab(rim):
#         rim_num = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }

#         ans = 0
#         for i in range(len(rim)-1):
#             if rim_num[rim[i]] < rim_num[rim[i+1]]:
#                 ans -= rim_num[rim[i]]
#             else:
#                 ans += rim_num[rim[i]]

#         ans += rim_num[rim[-1]]

#         return ans

# print(Solution.rim_to_arab("XIX"))
""""""
# class Pupil:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} - {self.age}"
    
#     def __add__(self, other):
#         return Pupil(self.name, self.age + other)
    
# p1 = Pupil("Yusuf", 16)
# print(p1)

# p1 += 1

# print(p1)

""""""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x} : {self.y})"

    def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)
        
point1 = Point(2, 3)
point2 = Point(4, 5)
    
result = point1 + point2

print(point1)
print(point2)
print(result)    