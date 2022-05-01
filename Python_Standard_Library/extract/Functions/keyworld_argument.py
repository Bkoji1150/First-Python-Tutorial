"""Key word arguement with python"""

def increment(number, by):
    return number + by 

result = increment(3, by=1)


"""Default aurgument """
def increment(number, by=1):
    return number + by 

result = increment(3)
print(result)