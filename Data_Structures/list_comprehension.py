"""Lambda function or expression, it's a one line """


items = [
   ( "Product1", 10),
    ("Product2", 14),
    ("Product3", 189)
]
"""here python doesn't know how to sort this items"""

x = list(map(lambda item: item[1], items))
print(x)
"""we can use list comprehension here"""
price = [item[1] for item in items]
print(price)

"""List get the list of object greater than 20"""
prices = list(filter(lambda item: item[1] > 20, items))
# print(prices)
filtered = [i for i in items if i[1] > 20]
print(filtered)