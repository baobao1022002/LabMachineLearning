from typing import List
from OrderItem import OrderItem
from datetime import date


class Order:

    def __init__(self, id: str, customer: str, employee: str, date: date, items: List[OrderItem]):
        self.id = id
        self.customer = customer
        self.employee = employee
        self.date = date
        self.items = items

