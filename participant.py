#!/usr/bin/python3

from card import Card
from deck import Deck

class Participant():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.deck = Deck(empty=True)

    def get_deck(self):
        return self.deck
    
    def take_card(self, card):
        self.deck.add_card(card)

    def get_num_of_cards(self):
        return len(self.deck)

    def throw_cards(self):
        self.deck.throw_cards()

    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return '[{} {}] Cards: {}'.format(self.first_name, self.last_name, str(self.get_deck()))

    def __eq__(self, other):
        if self.first_name == other.first_name and self.last_name == other.last_name:
            return True
        else:
            return False

class ParticipantTest():
    def __init__(self):
        p1 = Participant('John', 'Doe')
        for _ in range(10):
            p1.take_card(Card.random())
        print(p1)


def main():
    ParticipantTest()

if __name__ == '__main__':
    main()
