#!/usr/bin/python3

from deck import Deck
from card import Card
from participant import Participant

class Dealer(Participant):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def deal_card_from_deck(self, deck, player, is_visible=True):
        card = deck.pop_card(is_visible)
        if card is None:
            return
        else:
            player.take_card(card)

    def deal_cards_from_deck(self, deck, player, ncards=1, is_visible=True):
        for _ in range(ncards):
            self.deal_card_from_deck(deck, player, is_visible)
    
    def flip_card(self, idx=0, is_visible=True):
        deck = self.get_deck()
        card = deck.get_card(idx)
        card.set_visible(True)


    def __str__(self):
        return "[D]" + super().__str__()

class DealerTest():
    def __init__(self):
        from player import Player
        dlr = Dealer('John', 'Doe')
        dck = Deck(shuffle=True)
        plr = Player('Daniel', 'Negreanu', 1000)
        for _ in range(2):
            dlr.deal_cards_from_deck(dck, plr)
            dlr.deal_cards_from_deck(dck, dlr)
        print(dlr)
        print(plr)
        

def main():
    DealerTest()

if __name__ == '__main__':
    main()
