from typing import List


class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity: int) -> bool:
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        print(f"{self.name} bazada yetarlicha mavjud emas.")
        return False


class Customer:
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.balance = balance

    def deduct_balance(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
            return
        print(f"{self.name} balansida mablag' yetarli emas ({self.balance}).")


class Item:
    def __init__(self, product: Product, quantity: int) -> None:
        if not product.reduce_stock(quantity):
            raise ValueError(f"{product.name} yetarlicha mavjud emas.")
        self.product = product
        self.quantity = quantity


class Order:
    def __init__(self, customer: Customer) -> None:
        self.customer = customer
        self.items: List[Item] = []

    def add_item(self, product: Product, quantity: int) -> None:
        self.items.append(Item(product, quantity))

    def calculate_total(self) -> float:
        return sum(item.product.price * item.quantity for item in self.items)

    def complete_order(self) -> None:
        total = self.calculate_total()
        if not self.customer.deduct_balance(total):
            print("Buyurtma yakunlanmadi — balans yetarli emas.")
        else:
            print(f"Buyurtma yakunlandi. Jami summa: {total}")


class Shop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.products: List[Product] = []
        self.customers: List[Customer] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def add_customer(self, customer: Customer) -> None:
        self.customers.append(customer)
