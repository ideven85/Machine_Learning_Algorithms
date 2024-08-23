from cards import Suit, Card, AceCard, FaceCard


# todo Practice lambda, map, filter reduce
def card_lambda(rank: int, suit: Suit) -> Card:
    class_ranks = {
        1: lambda suit: AceCard("A", suit),
        11: lambda suit: FaceCard("J", suit),
        12: lambda suit: FaceCard("Q", suit),
        13: lambda suit: FaceCard("K", suit),
    }.get(rank, lambda suit: Card(str(rank), suit))
    return class_ranks(suit)


print(card_lambda(1, Suit.Spade))
