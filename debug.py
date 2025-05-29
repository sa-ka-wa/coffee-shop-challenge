from customer import Customer
from coffee import Coffee

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
mocha = Coffee("Mocha")

# Create orders
alice.create_order(latte, 4.5)
alice.create_order(mocha, 5.0)
bob.create_order(latte, 6.0)

# Test relationships
print("Alice's Orders:", alice.orders())
print("Alice's Coffees:", [c.name for c in alice.coffees()])
print("Latte Orders:", latte.orders())
print("Latte Customers:", [c.name for c in latte.customers()])
print("Latte Average Price:", latte.average_price())

# Most Aficionado
print("Most Aficionado for Latte:", Customer.most_aficionado(latte).name)
