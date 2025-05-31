class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._orders = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 3 <= len(value) <= 20:
            self._name = value
        else:
            raise ValueError("Name must be a string between 3 and 20 characters.")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a number between 1.0 and 10.0.")

    def num_orders(self):
        return len(self._orders)

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)

