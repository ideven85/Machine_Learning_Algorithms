# strategy_best2.py
# Strategy pattern -- function-based implementation
# selecting best promotion from current module globals

"""
    >>> joe = Customer('John Doe', 0)
    >>> ann = Customer('Ann Smith', 1100)
    >>> cart = [LineItem('banana', 4, .5),
    ...         LineItem('apple', 10, 1.5),
    ...         LineItem('watermelon', 5, 5.0)]
    >>> Order(joe, cart, fidelity_promo)
    <Order total: 42.00 due: 42.00>
    >>> Order(ann, cart, fidelity_promo)
    <Order total: 42.00 due: 39.90>
    >>> banana_cart = [LineItem('banana', 30, .5),
    ...                LineItem('apple', 10, 1.5)]
    >>> Order(joe, banana_cart, bulk_item_promo)
    <Order total: 30.00 due: 28.50>
    >>> long_cart = [LineItem(str(item_code), 1, 1.0)
    ...               for item_code in range(10)]
    >>> Order(joe, long_cart, large_order_promo)
    <Order total: 10.00 due: 9.30>
    >>> Order(joe, cart, large_order_promo)
    <Order total: 42.00 due: 42.00>

# tag::STRATEGY_BEST_TESTS[]

    >>> Order(joe, long_cart, best_promo)
    <Order total: 10.00 due: 9.30>
    >>> Order(joe, banana_cart, best_promo)
    <Order total: 30.00 due: 28.50>
    >>> Order(ann, cart, best_promo)
    <Order total: 42.00 due: 39.90>

# end::STRATEGY_BEST_TESTS[]
"""

from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f"<Order total: {self.total():.2f} due: {self.due():.2f}>"


def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


# tag::STRATEGY_BEST2[]

promos = [
    globals()[name]
    for name in globals()  # <1>
    if name.endswith("_promo") and name != "best_promo"  # <2>
]  # <3>


def best_promo(order):
    """Select best discount available"""
    return max(promo(order) for promo in promos)  # <4>


# end::STRATEGY_BEST2[]
