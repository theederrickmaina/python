import datetime
class product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity_in_stock = quantity_in_stock
        
    def display_info(self):
        print("Product ID:", self.product_id)
        print("Product name:", self.product_name)
        print("Product stock:", self.quantity_in_stock)
        
    def update_stock(self, quantity):
        if quantity >= 0:
            self.quantity_in_stock += quantity
            print("Stock increased for", self.product_name, ":", self.quantity_in_stock) 
        else:
            if abs(quantity) <=self.quantity_in_stock:
                self.quantity_in_stock -= abs(quantity)
                print("Stock decreases for", self.product_name, ":", self.quantity_in_stock) 
            else:
                print("Not enough stock available", self.product_name)
    
    def calculate_value(self):
        return self.quantity_in_stock


product1 = product("001", "RAM 8GB DDR4", 60)
product1.display_info()
print("Total value of product 1:", product1.calculate_value())

product2 = product("002", "hp 360 laptop", 10)
product2.display_info()
print("Total value of product 2:", product2.calculate_value())

product3 = product("003", "Bread", 30)
product3.display_info()
print("Total value of product 3:", product3.calculate_value())

product4 = product("004", "Wheat flour", 50)
product4.display_info()
print("Total value of product 4:", product4.calculate_value())

product5 = product("005", "512GB SSD", 100)
product5.display_info()
print("Total value of product 5:", product5.calculate_value())


class SimpleProduct(product):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price):
        super().__init__(product_id, product_name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

product1 = SimpleProduct("001", "RAM 8GB DDR4", 60, 5000)
product1.display_info()    
print("Total value of product 1:", product1.calculate_value())

product2 = SimpleProduct("002", "hp 360 laptop", 10, 30000)
product2.display_info()
print("Total value of product 2:", product2.calculate_value())

product3 = SimpleProduct("003", "Bread", 30, 65)
product3.display_info()
print("Total value of product 3:", product3.calculate_value())

product4 = SimpleProduct("004", "Wheat flour", 50, 80)
product4.display_info()
print("Total value of product 4:", product4.calculate_value())

product5 = SimpleProduct("005", "512GB SSD", 100, 50)
product5.display_info()
print("Total value of product 5:", product5.calculate_value())

class PerishableProduct(product):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, product_name, quantity_in_stock)
        self.unit_price = unit_price
        self.expiry_date = expiry_date

    def calculate_value(self):
        remaining_shelf_life = self.expiry_date - datetime.date.today()
        discount = 1.0
        if remaining_shelf_life.days <= 30:
            discount = 0.8
        elif remaining_shelf_life.days <= 60:
            discount = 0.9
        
        total_value = self.quantity_in_stock * self.unit_price * discount
        return total_value
    
print("PERISHABLE PRODUCTS")
product1 = PerishableProduct("006", "Milk", 100, 20, datetime.date(2024, 4, 30))
product1.display_info()
print("Total value of product 6:", product1.calculate_value())

product2 = PerishableProduct("007", "Yogurt", 50, 15, datetime.date(2024, 5, 15))
product2.display_info()
print("Total value of product 7:", product2.calculate_value())

product3 = PerishableProduct("008", "Cheese", 80, 30, datetime.date(2024, 5, 30))
product3.display_info()
print("Total value of product 8:", product3.calculate_value())
            
class DigitalProduct(product):
    def __init__(self, product_id, product_name, quantity_in_stock, price):
        super().__init__(product_id, product_name, quantity_in_stock)
        self.price = price

    def calculate_value(self):
        return self.quantity_in_stock * self.price
    
print("DIGITAL PRODUCTS")
product6 = DigitalProduct("009", "Hinses TV", 100, 90000)
product6.display_info()
print("Total value of product 9:", product6.calculate_value())

product7 = DigitalProduct("010", "MAC Book computer", 200, 176000)
product7.display_info()
print("Total value of product 10:", product7.calculate_value())