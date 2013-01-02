import math


def average(data): 
    return sum(data) * 1.0 / len(data)
def stdev(data,average):
    std=0
    for point in data:
        std = std + (point - average)**2
        std = math.sqrt(std / len(data))
    return std
       
''' 
print average([1,2,3,4,5,6])
'''