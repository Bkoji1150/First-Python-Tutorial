"""Lambda function or expression, it's a one line """


items = [
   ( "Product1", 10),
    ("Product2", 14),
    ("Product3", 189),
    ("Product4", 20),
    ("Product5", 30),
]
"""here python doesn't know how to sort this items"""
# items.sort()
price = list(filter(lambda item: item[1] >= 20, items))
print(price)
# x = list(filter(lambda item: item[1] >= 20, items))
# price = []

# for item in items:
#     price.append(item[1])
# for x in price:    
#     if x > 20:
#         print(f"prices greater than 20 {x}")   
#     else:
#         print(f"not greater than {x}")

"""Lambda function or expression, it's a one line """
price = list(map(lambda item:item[1], items))
# print(price)
