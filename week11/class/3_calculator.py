import random

class Calculator:
    def __init__(self,list=[]):
        self.__list = list

    def get_average(self):
        total = 0
        for item in self.__list:
            total +=item
        return total/len(self.__list)

    def get_min(self):
        min_val = self.__list[0]
        for item in self.__list:
            if item < min_val:
                min_val = item
        return min_val

    def get_max(self):
        max_val = self.__list[0]
        for item in self.__list:
            if item > max_val:
                max_val = item
        return max_val

    def clear(self):
        self.__list.clear()
        print(self.__list)

    def generate_random_data(slef,x,y,z):
        r_list = []
        for w in range(x):
            r_list.append(random.randint(y, z))
        return r_list



a_list = [2,3,4,5]
c = Calculator(a_list)
print("Average: {}".format(c.get_average()))
print("min: {}".format(c.get_min()))
print("max: {}".format(c.get_max()))
r_list = c.generate_random_data(3,10,100)
print("random_data: {}".format(r_list))

