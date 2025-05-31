class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 1.0:  # Assuming minimum valid price is 1.0
            raise ValueError("Price must be at least 1.0")
        if price > 10.0:  # assuming 10 is max valid price
            raise ValueError("Price must be at most 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
