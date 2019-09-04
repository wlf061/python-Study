from .card import card10
import random

"""
通过 Deck 类的 内部实际是list,Deck 类的pop方法只是对 list 对象 响应函数的调用 
"""
class Deck:
    def __init__(self):
        self._cards = [card10(r+1,s) for r in range(13) for s in ("Club","Diamond","Heart","Spade")]
        random.shuffle(self._cards)
        return self._cards.pop()


""" 
Deck 类可以继承自 list, 简化代码
"""

class Deck2(list):
    def __init(self):
        super().__init__(card10(r+1,s) for r in range(13) for s in ("Club","Diamond","Heart","Spade") )
        random.shuffle(self)