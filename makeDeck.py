# to make a poker deck without Jokers
from collections import namedtuple

class Deck:
    def __str__(self) -> str:
        return f"This is to make a poker deck without Jokers"
    
    def make_deck(self):
        suits = "spade heart diamond club".split()
        ranks = [i for i in range(2,11)]
        ranks.extend("JQKA")
        Poker = namedtuple("Poker", ["rank", "suit"])
        card = [ Poker(rank, suit) for suit in suits for rank in ranks ]
        return card