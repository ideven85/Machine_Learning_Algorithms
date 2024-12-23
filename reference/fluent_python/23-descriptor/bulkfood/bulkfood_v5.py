"""

A line item for a bulk food order has description, weight and price fields::

    >>> raisins = LineItem('Golden raisins', 10, 6.95)
    >>> raisins.weight, raisins.description, raisins.price
    (10, 'Golden raisins', 6.95)

A ``subtotal`` method gives the total price for that line item::

    >>> raisins.subtotal()
    69.5

The weight of a ``LineItem`` must be greater than 0::

    >>> raisins.weight = -20
    Traceback (most recent call last):
        ...
    ValueError: weight must be > 0

No change was made::

    >>> raisins.weight
    10

Negative or 0 price is not acceptable either::

    >>> truffle = LineItem('White truffle', 100, 0)
    Traceback (most recent call last):
        ...
    ValueError: price must be > 0

If the descriptor is accessed in the class, the descriptor object is
returned:

    >>> LineItem.weight  # doctest: +ELLIPSIS
    <model_v5.Quantity object at 0x...>
    >>> LineItem.weight.storage_name
    'weight'

The `NonBlank` descriptor prevents empty or blank strings to be used
for the description:

    >>> br_nuts = LineItem('Brazil Nuts', 10, 34.95)
    >>> br_nuts.description = ' '
    Traceback (most recent call last):
        ...
    ValueError: description cannot be blank
    >>> void = LineItem('', 1, 1)
    Traceback (most recent call last):
        ...
    ValueError: description cannot be blank


"""

# tag::LINEITEM_V5[]
import model_v5 as model  # <1>


class LineItem:
    description = model.NonBlank()  # <2>
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


# end::LINEITEM_V5[]
