from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional

#todo Subclassing NamedTuple.. just revisit that
class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    price: float
    quantity: int

    def total(self):
        return self.price * self.quantity


class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional["Promotion"] = None

    def total(self):
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self):
        if not self.promotion:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount


class Promotion(ABC):
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Return Discount as Positive Dollar Amount"""


class LoyaltyPromotion(Promotion):
    """5 % discount if fidelity exceeds 1000 points"""

    def discount(self, order: Order) -> Decimal:
        rate = Decimal("0.05")

        if order.customer.fidelity >= 1000:
            return order.total() * rate
        return Decimal(0)


class WholeSalePromotion(Promotion):
    """10% discount if order quantity exceeds 20"""

    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal("0.1")
        return discount
