numbers = [3,51, 2, 8, 6]
if "d" in numbers:
    print("yes")
# print(numbers.index(0))

# sort a list 

numbers.sort(reverse=True)



items = [
   ( "Product1", 10),
    ("Product2", 14),
    ("Product3", 189)
]
"""here python doesn't know how to sort this items"""
items.sort()


def sort_items(items):
    return items[1]

"""sort based on the lowest price"""
items.sort(key=sort_items)    
print(items)



