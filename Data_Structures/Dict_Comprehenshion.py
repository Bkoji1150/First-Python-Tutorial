values = []

for x in range(5):
    values.append(x * 2)
# print(values)  

"""similarly"""
values = (x * 2 for x in range(5))
# print(values)

"""unpacking object"""
number = [1,2,3,4,5]

print(*number)