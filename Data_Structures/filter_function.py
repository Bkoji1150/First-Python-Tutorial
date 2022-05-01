"""filter this list and get the price greater than "20"""
items = [
   ( "Product1", 10),
    ("Product2", 14),
    ("Product3", 25),
    ("Product4", 189)
]
"""Lambda parameter and expression"""
price = []
'''
for item in items:
    
    if item[1] > 20:
        print(items[1])
'''        

"""filter"""
x = list(filter(lambda item: item[1] >= 20, items))
print(x)