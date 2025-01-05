"""
Следующий пример очень прост, однако демонстрирует выгоды от реализации
двух специальных методов: __getitem__ и __len__.
"""
from dataclasses import dataclass
from collections import namedtuple
from random import choice


# Card = namedtuple('Card', 'rank suit')
# в книге объект Card реализован с помощью namedtuple,
# но я реализую его с помощью dataclass:

@dataclass(frozen=True, slots=True)
class Card:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades clubs diamonds hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


deck = FrenchDeck()
print(len(deck))
print(choice(deck))
print(choice(deck))
print(choice(deck))
print(choice(deck))
print(choice(deck))
print(choice(deck))
# как только был реализован метод __getitem__ колода стала
# допускать итерирование:
print('----------------')
for card in deck:
    print(card)
