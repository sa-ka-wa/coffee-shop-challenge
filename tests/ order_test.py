class Order:
    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee

        self.customer = customer
        self.coffee = coffee
        self._set._price(price)

    def _set_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = float(value)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        raise AttributeError("Price is immutable and cannot be changed once set")