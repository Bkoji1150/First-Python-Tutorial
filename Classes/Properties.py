"""how to prevent a value from having a negative price"""
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price 
        
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative.")
        self.__price = value

    price = property(get_price, set_price)  

product = Product(-10)
price = product.price
print(price)