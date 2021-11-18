import random

class DataGenerator:
    def __init__(self,numOfValues = 10, rangeStart = 0, rangeEnd = 1):
        self.numOfValues = numOfValues
        self.rangeStart = rangeStart
        self.rangeEnd = rangeEnd

#testing code for class
#     def generate(self):
#         for x in range(self.numOfValues):
#             print(random.randint(self.rangeStart, self.rangeEnd))

# x = DataGenerator(5, 0, 10)
# x.generate()
