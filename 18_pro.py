# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price.
#  Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self,price):
        self.__price = price # private attribute

    @property
    def price(self):
        return self.__price
        
    @price.setter
    def price(self, value):
        self.__price = value
        return self.__price
    
    @price.deleter
    def price(self):
        del self.__price

product1 : Product = Product(1000)
print(product1.price) 
product1.price = 2000
print(product1.price)
product1.price = 3000
print(product1.price) # 


del product1.price  # delete the price
print('product1 price deleted successfully') # This will not print the price as it is deleted

   
   
      



        