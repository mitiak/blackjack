#!/usr/bin/python3
from random import shuffle, choice

class Card():

    # Card ranks
    low_ranks = [x for x in range(2, 11)]
    high_ranks = ['j', 'q', 'k', 'a']
    ranks = low_ranks + high_ranks

    # Card suits
    suits = ['spades', 'clubs', 'hearts', 'diamonds']

    # Suits and ranks textual representation
    ranks_str = {2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 
                7:'seven', 8:'eight', 9:'nine', 10:'ten', 'j':'jack', 
                'q':'queen', 'k':'king', 'a':'ace'}

    # suits unicode
    suits_uni = {   'spades' : u'\u2660', 
                    'clubs' : u'\u2663', 
                    'hearts' : u'\u2665', 
                    'diamonds' : u'\u2666'}

    def __init__(self, rank, suit, is_visible=True):
        self.rank = rank
        self.suit = suit
        self.is_visible = is_visible

    def __str__(self):
        if self.is_visible:
            return '[{}{}]'.format(self.rank, Card.suits_uni[self.suit])
        else:
            return '[XX]'
    
    def set_visible(self, is_visible=True):
        self.is_visible = is_visible

    def __repr__(self):
        if self.is_visible:
            return '{} of {}'.format(Card.ranks_str[self.rank], self.suit)
        else:
            return '??'

    
    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank
    
    @classmethod
    def random(cls, is_visible=True):
        rank = choice(Card.ranks)
        suit = choice(Card.suits)
        return cls(rank, suit, is_visible)

class CardTest():
    def __init__(self):
        c1 = Card.random()
        print(c1)
        print(c1, repr(c1))

        c2 = Card.random(False)
        print(c2)
        print(c2, repr(c2))


def main():
    CardTest()

if __name__ == '__main__':
    main()
