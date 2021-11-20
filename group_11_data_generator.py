import random
import matplotlib.pyplot as plt
import numpy as np


class DataGenerator:
    def __init__(self, num_vals=10, range_start=0, range_end=1):
        self.num_vals = num_vals
        self.range_start = range_start
        self.range_end = range_end

    def __gen_points(self):
        return np.array([random.random() for _ in range(self.num_vals)])

    def data_in_range(self):
        return (self.range_end - self.range_start) * self.__gen_points() + self.range_start

    def plot(self, points):
        plt.plot(points, color='g')
        plt.xlabel("Day of Month (Nov)")
        plt.ylabel("Price ($)")
        plt.title("Stock Prices")
        plt.show()


if __name__ == '__main__':
    gen = DataGenerator(30, 112, 125)
    data = gen.data_in_range()
    gen.plot(data)
