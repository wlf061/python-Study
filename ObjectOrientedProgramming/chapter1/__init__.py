class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.sort = self._points()


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    def _points(self):
        return 1, 11


class FaceCard(Card):
    def points(self):
        return 10, 10


def card4(rank,suit):
    """
     通过rank 到 类的映射来实现工厂类
     语句功能说明：{1:AceCard,11:FaceCard,12:FaceCard,13:FaceCard}.get(rank, NumberCard)， 通过 key=rank 来获取value, 如果 key 不存在，则返回NumberCard
    """

    class_={1:AceCard,11:FaceCard,12:FaceCard,13:FaceCard}.get(rank, NumberCard)
    return class_(rank, suit)

"""
基于card4 有需求的变更： 返回Card 子类的同时，还需要提供rank对象的字符串结果, 通过card5来实现
"""
def card5(rank,suit):
    class_={1:AceCard,11:FaceCard, 12:FaceCard,13:FaceCard}.get(rank,NumberCard)
    rank_str = {1:'A',11:'J',12:'Q',13:'K'}.get(rank, str(rank))
    return class_(rank_str,suit)

""""
 card5 存在的问题是使用的是并行映射， 并行映射存在的问题是后面改动会存在维护成本； 通过card6 的元组来实现 
"""
def card6(rank, suit):
    class_, rank_str = {
        1: (AceCard,'A'),
        11: (FaceCard,'J'),
        12: (FaceCard,' Q'),
        13: (FaceCard,'K'),
    }.get(rank,(NumberCard,str(rank)))
    return class_(rank_str,suit)



if __name__ == '__main__':
    card4(1,"test")