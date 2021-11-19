import random
import matplotlib
import matplotlib.pyplot as plt

class DataGenerator:
    def __init__(self,numOfValues = 10, rangeStart = 0, rangeEnd = 1):
        self.numOfValues = numOfValues
        self.rangeStart = rangeStart
        self.rangeEnd = rangeEnd

    def __randomNormalizer(self):
        randomNum = random.gauss(self.rangeStart,self.rangeEnd)
        return randomNum

    def getDataInRange(self):
        return (self.rangeEnd-self.rangeStart)*(self.__randomNormalizer())+(self.rangeStart)

#test code for class
#x = DataGenerator(5,0,10)
#print(x.getDataInRange())
