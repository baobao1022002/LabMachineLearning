from Product import Product


class OrderItem:
    def __init__(self, item: Product, amount: int):
            self.item = item
            self.amount = amount

