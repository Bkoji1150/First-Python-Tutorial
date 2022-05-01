"""combine multiple list as tuple"""

list1 = ["product1", "product2","product3", "product4"]
list2 = [10,20,30,40]

"""zip"""
# [("product1", 10), ("product2", 20), ("product3", 30), ("product4", 40)]
print(list(zip("azcvf", list1, list2)))