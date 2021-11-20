import random
import matplotlib
import matplotlib.pyplot as plt

class DataGenerator:
    def __init__(self,numOfValues = 10, rangeStart = 0, rangeEnd = 1):
        self.numOfValues = numOfValues
        self.rangeStart = rangeStart
        self.rangeEnd = rangeEnd

    def __randomGenerator(self):
        randomNum = random.randint(self.rangeStart,self.rangeEnd)
        return randomNum

    def __randomPlotGenerator(self, minVal, maxVal):
        randomArr=[self.__randomGenerator(minVal,maxVal) for num in range(self.numOfValues)]
        return randomArr

    def getDataInRange(self):
        return (self.rangeEnd-self.rangeStart)*(self.__randomPlotGenerator(self.rangeStart, self.rangeEnd))+(self.rangeStart)

#test code for class
# x = DataGenerator()
#print(x.getDataInRange())
# print(x)
