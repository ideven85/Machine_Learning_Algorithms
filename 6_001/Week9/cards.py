from collections import namedtuple

#
# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#
#     def __str__(self):
#         return 'Card'

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = list(str(range(2, 11))) + ["J", "Q", "K", "A"]
    suits = ['hearts', 'spades', 'clubs', 'diamonds']

    def __init__(self):
        self._deck = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __getitem__(self, position):
        return self._deck[position]

    def __len__(self):
        return len(self._deck)


if __name__ == '__main__':
    """
    >>> beer_card = Card('7', 'diamonds')
    >>> beer_card
    Card(rank='7', suit='diamonds')
    """
    beer_card = Card('7', 'diamonds')  # How??
    print(beer_card)
    # doctest.testmod(verbose=True)
