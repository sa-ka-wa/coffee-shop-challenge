class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._coffees = []
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return list(self._orders)
    
    def coffees(self):
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        from order import Order 
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order
    @classmethod
    def most_aficionado(cls, coffee):
        max_spent = 0
        top_customer = None
        for order in coffee.orders():
            customer = order.customer
            total_spent = sum(o.price for o in order.customer.orders() if o.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = order.customer
        return top_customer