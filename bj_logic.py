#!/usr/bin/python3

from deck import Deck
from card import Card
from player import Player

class BJLogic():
    @staticmethod
    def get_card_score(card):
        rank = card.get_rank()
        if not card.is_visible:
            return 0
        if rank in Card.low_ranks:
            return rank
        elif rank == 'a':
            return 11  
        else:
            return 10
            
    @classmethod
    def get_deck_score(cls, deck):
        score = 0 
        for card in deck.cards:
            score += cls.get_card_score(card)
        return score

    @classmethod
    def get_player_score(cls, player):
        return cls.get_deck_score(player.deck)


class LogicTest():
    def __init__(self):
        p1 = Player('Daniel', 'Negreanu', 1000)
        for _ in range(5):
            p1.take_card(Card.random())
            print(str(p1) + ', Score:', BJLogic.get_player_score(p1))

def main():
    LogicTest()

if __name__ == '__main__':
    main()

