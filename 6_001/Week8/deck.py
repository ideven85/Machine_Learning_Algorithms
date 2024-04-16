from collections import namedtuple

cards = ("Card", ["Rank", "Suit"])
print(cards)
Card = namedtuple("Cards", ["Rank", "Suit"])


class Deck:
    ranks = [str(i) for i in range(2, 11)] + ["J", "K", "Q", "A"]
    suits = ["spades", "diamonds", "hearts", "clubs"]

    def __init__(self):
        self._cards = [Card(y, x) for x in self.suits for y in self.ranks]

    def __getitem__(self, index):
        return self._cards[index]

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return "Hi"


deck = Deck()
card = deck[2]
# print([x for x in deck])
print(deck[-4:])
# print(deck.ranks.index(card.Suit))


def custom_sort(card):
    suit_ranks = {"spades": 3, "diamonds": 2, "hearts": 1, "clubs": 0}
    card_rank = Deck.ranks.index(card.Rank)
    return card_rank * 4 + suit_ranks[card.Suit]


sorted_deck = sorted(deck, key=custom_sort, reverse=True)
print(sorted_deck[-4:])
