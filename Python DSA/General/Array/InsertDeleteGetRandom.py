# from collections import defaultdict
# import random

# class RandomizedSet:

#     def __init__(self):
#         self.values = defaultdict(int)
#         self.valArr = []
#         self.index = 1
#         self.length = 0
#         self.randomIndex = 0

#     def insert(self, val: int) -> bool:
#         if self.values[val] == 0:
#             self.values[val] = self.index
#             self.valArr.append(val)
#             self.index += 1
#             self.length += 1
#             return True
#         return False

#     def remove(self, val: int) -> bool:
#             i = self.values[val]
#             if i != 0:
#                 lastVal = self.valArr[-1]
#                 self.valArr[self.values[val]-1] = lastVal
#                 self.values[lastVal] = i
#                 self.valArr.pop()
#                 self.index -= 1
#                 self.values[val] = 0
#                 self.length -= 1
#                 return True
#             return False

#     def getRandom(self) -> int:
#         if self.randomIndex >= self.length:
#             self.randomIndex = 0
#         arr = self.valArr[self.randomIndex:]
#         self.randomIndex += 1
#         return random.choice(arr)
    
# r = RandomizedSet()
# r.insert(0)
# r.insert(1)
# print(r.valArr)
# r.remove(0)
# print(r.valArr)
# r.insert(2)
# r.remove(1)
# print(r.valArr)
# print(r.getRandom())

print("fee"*10)