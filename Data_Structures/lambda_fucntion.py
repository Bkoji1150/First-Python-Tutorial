"""Lambda function or expression, it's a one line """


items = [
   ( "Product1", 10),
    ("Product2", 14),
    ("Product3", 189)
]
"""here python doesn't know how to sort this items"""
items.sort()

'''
def sort_items(items):
    return items[1]
'''
"""key= lambda parameter: expression"""

items.sort(key=lambda items:items[0])
print(items)