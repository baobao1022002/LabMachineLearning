from typing import List, Dict

from OrderItem import OrderItem
from Product import Product
from Order import Order
from datetime import date


class OrderManager:


    def __init__(self, orders: List[Order]):
        self.orders = orders

    def get_product_with_highest_price(self) -> Product:

        highest_price_product = None
        highest_price = 0
        for order in self.orders:
            for order_item in order.items:
                if order_item.item.price > highest_price:
                    highest_price = order_item.item.price
                    highest_price_product = order_item.item
        return highest_price_product

    def test_get_product_with_highest_price(self):
        """
        Test the get_product_with_highest_price method by printing the name of the product with the highest price.
        """
        highest_price_product = self.get_product_with_highest_price()
        print("The product with the highest price is:", highest_price_product.name)

    def num_products_by_type(self) -> Dict[str, int]:
        products_by_type = {}
        for order in self.orders:
            for order_item in order.items:
                product_type = order_item.item.type
                if product_type in products_by_type:
                    products_by_type[product_type] += order_item.amount
                else:
                    products_by_type[product_type] = order_item.amount
        return products_by_type

    def test_num_products_by_type(self):
        self.num_products_by_type()
        print("Perform statistical task to show the number of products bought by each type of product", self.num_products_by_type())


product1 = Product("Apple", "Fruit", 2, date(2023, 3, 1))
product2 = Product("Banana", "Fruit", 3, date(2023, 3, 2))
product3 = Product("Milk", "Dairy", 4, date(2023, 3, 3))
product4 = Product("Cheese", "Dairy", 5, date(2023, 3, 4))

# Create some order items
order_item1 = OrderItem(product1, 2)
order_item2 = OrderItem(product2, 3)
order_item3 = OrderItem(product3, 4)
order_item4 = OrderItem(product4, 5)

# Create some orders
order1 = Order("1", "Customer 1", "Employee 1", date(2023, 3, 1), [order_item1, order_item2])
order2 = Order("2", "Customer 2", "Employee 2", date(2023, 3, 2), [order_item3, order_item4])
order3 = Order("3", "Customer 3", "Employee 3", date(2023, 3, 3), [order_item1, order_item4])

# Create an order manager and add the orders to it
order_manager = OrderManager([order1, order2, order3])

# Test the get_product_with_highest_price method
order_manager.test_get_product_with_highest_price()

order_manager.test_num_products_by_type()
# products_by_type = order_manager.num_products_by_type()
# print(products_by_type)
