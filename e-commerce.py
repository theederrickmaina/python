def add_product(product_name, price, quantity): 
     product = {
        'product_name': product_name,
        'price': price,
        'quantity': quantity
    }
     return product

def update_price(product, new_price):
     product['price'] = new_price
     return product

def update_quantity(product, quantity_change):
     product['quantity'] += quantity_change
     return product

product1 = add_product("Laptop", 50000, 10)
product2 = add_product("512GB SSD", 8000, 30)

print("Original Products:")
print(product1)
print(product2)

product1 = update_price(product1, 55000)
product2 = update_price(product2, 9000)
print("\nUpdated Product (price):")
print(product1)
print(product2)

product1 = update_quantity(product1, 5)
product2 = update_quantity(product2, -10) 
print("\nUpdated Products (Quantity):")
print(product1)
print(product2)