from enum import Enum
from typing import Tuple

class Suit(str,Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"

class Card:
    def __init__(self, rank:str,suit:str)->None:
        self.rank = rank
        self.suit = suit
        self._hard, self._soft = self._points()  # Not initialized directly

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)

    # def __str__(self):
    #     return str(self._hard),str(self._soft)

class AceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 1, 11


class JackCard(Card):
    def _points(self):
        return 11, 11




class FaceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 10, 10
cards = [AceCard('A', Suit.Spade), Card('2',Suit.Club), FaceCard('J',Suit.Heart)]
print(cards)
x = Card('2', '♠')
#x = Card('2', Suit.Heart)
print(x)
