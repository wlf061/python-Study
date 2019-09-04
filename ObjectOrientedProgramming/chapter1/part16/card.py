class Card:
    def __init__(self,rank,suit,hard,soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft
class NumberCard(Card):
    def __init__(self,rank,suit):
        super().__init__(str(rank),suit,rank,rank)
class AceCard(Card):
    def __init__(self,rank,suit):
        super().__init__("A",suit,rank,rank)
class FaceCard(Card):
    def __init__(self,rank,suit):
        super().__init__({11:'J',12:'Q',13:'K'}[rank],suit,rank,rank)



def card10(rank,suit):
    if rank == 1: return AceCard(rank,suit)
    elif 2 <= rank < 11: return NumberCard(rank,suit)
    elif 11 <= rank < 14: return FaceCard(rank,suit)
    else:
        raise Exception("Rank out of range")