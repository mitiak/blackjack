#!/usr/bin/python3

from random import shuffle
from card import Card

class Deck():
    def __init__(self, **kw):
        self.cards = []
        self.cur_ncards = 0

        if kw.get("empty") == True:
            return
        else:
            for rank in Card.ranks:
                for suit in Card.suits:
                    self.add_card(Card(rank, suit))

        if kw.get("shuffle") == True:
            self.shuffle()

    def add_card(self, card):
        self.cards.append(card)
        self.cur_ncards += 1

    def __str__(self):
        if self.is_empty():
            return '0 cards'
        deck_str = str(self.__len__()) + " cards: "

        for card in self.cards:
            deck_str += str(card)
        return deck_str

    def __len__(self):
        return self.cur_ncards
    
    def shuffle(self):
        shuffle(self.cards)

    def is_empty(self):
        return self.cur_ncards == 0

    def get_card(self, idx=0):
        return self.cards[idx]
    
    def pop_card(self, is_visible=True):
        if self.is_empty():
            return None
        card = self.cards.pop(0)
        card.set_visible(is_visible)
        self.cur_ncards -= 1
        return card

class DeckTest():
    def __init__(self):
        # create a new deck
        d1 = Deck(shuffle=True, empty=False)
        print(d1)

        for _ in range(5):
            c = d1.pop_card()
            if c is not None:
                print(c)
        print(d1)


def main():
    DeckTest()

if __name__ == '__main__':
    main()