from models import Product, Customer, Order, Shop

# Do‘kon yaratish
shop = Shop("TechStore")

# Mahsulotlar
laptop = Product("Laptop", 1200, 5)
mouse = Product("Mouse", 25, 30)
shop.add_product(laptop)
shop.add_product(mouse)

# Xaridor
user = Customer("Ali", 2000)
shop.add_customer(user)

# Buyurtma yaratish
order = Order(user)
order.add_item(laptop, 1)
order.add_item(mouse, 2)

# Umumiy summa
print("Total:", order.calculate_total())

# Buyurtmani yakunlash
order.complete_order()

# yana qo'shimcha sifatida chiqardim
print("Yangi balans:", user.balance)
print("Laptop zaxirasi:", laptop.stock)
print("Mouse zaxirasi:", mouse.stock)
