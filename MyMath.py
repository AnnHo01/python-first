import math

class MyMath():
    """This class contains function to perform Max, Average, and standard Deviation of a list of number"""
    def __init__(self):
        self.num_list = []

    def max(self):
        """This function returns the highest number of a list of given number"""
        max = 0
        for num in self.num_list:
            if(max < num):
                max = num

        return max

    def avg(self):
        """This function returns the average of a list of number."""
        num_sum = 0
        for num in self.num_list:
            num_sum = num_sum + num
        avg = num_sum/len(self.num_list)
        return avg

    def std_dev(self):
        """This function returns the standard deviation of a number."""
        num_sum = 0
        for i in range(10):
            num_sum = num_sum + ((i + 1) - self.avg())**2

        deviation = num_sum/(len(self.num_list) - 1)
        deviation = math.sqrt(deviation)
        return self.truncate(deviation, 3)

    def truncate(self, float_num, num):
        """This function round down given number based on number of decimal places wanted."""
        return math.floor(float_num * 10 ** num) / 10 ** num

# test1 = MyMath()

# while True:
#     inp = input("Please enter a number. Enter d when you're done: ")
#     if inp.lower() == "d" or inp == "":
#         break
#     test1.num_list.append(float(inp))

# print(f"Your max is: {test1.max()} \nYour average is: {test1.avg()} \nYour standard deviation is: {test1.std_dev()}")