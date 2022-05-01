numbers = [3,51, 2, 8, 6]

print(dir(numbers))
 
"""adding object in the list"""

numbers.append('d')
numbers.insert(0, "bello")

# Removing object in a list 

numbers.pop(0)
numbers.remove('d')
del numbers[0:3]
numbers.clear()
print(numbers)