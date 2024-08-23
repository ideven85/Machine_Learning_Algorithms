from enum import Enum
from typing import Tuple


class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"


class Card:
    def __init__(self, rank: str, suit: Suit) -> None:
        self.rank = rank
        self.suit = suit
        self._hard, self._soft = self._points()  # Not initialized directly

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)

    def __str__(self):
        return f"{self.rank},{self.suit.value}"


class AceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 1, 11


class JackCard(Card):
    def _points(self):
        return 11, 11


class FaceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 10, 10


def card(rank: int, suit: Suit) -> Card:
    if rank == 1:
        return AceCard("A", suit)
    elif rank in range(2, 11):
        return Card(str(rank), suit)
    elif rank in range(11, 14):
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception("Not a valid card")

        # match r:
        #     case :
        #         return AceCard("A",suit)
        #     case [2,11]:
        #         return Card(str(rank),suit)
        #     case {11:"J",12:"Q",13:"K"}:
        #         return FaceCard()


def card2(rank: int, suit: Suit) -> Card:
    """
    Since class is a first-class object, we can easily map from the rank parameter to the
     class that must be constructed.
    """
    class_ = {1: AceCard, 12: FaceCard, 13: FaceCard, 14: FaceCard}.get(rank, Card)
    return class_(str(rank), suit)


def main():
    cards = [AceCard("A", Suit.Spade), Card("2", Suit.Club), FaceCard("J", Suit.Heart)]
    print(cards)
    # x = Card('2', '♠')
    x = Card("2", Suit.Heart)
    print(x)
    print(card(2, Suit.Spade)._points())
    deck = [
        card(rank, suit)
        for rank in range(1, 14)
        for suit in (Suit.Club, Suit.Diamond, Suit.Heart, Suit.Spade)
    ]


if __name__ == "__main__":
    main()
