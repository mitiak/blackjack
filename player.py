#!/usr/bin/python3

from deck import Deck
from card import Card
from participant import Participant

class Player(Participant):
    def __init__(self, first_name, last_name, bank):
        super().__init__(first_name, last_name)
        self.bank = bank

    def __str__(self):
        return "[P]" + super().__str__() + ", " + 'Bank: {.bank}'.format(self)

class PlayerTest():
    def __init__(self):
        p1 = Player('Daniel', 'Negreanu', 1000)
        print(p1)
        for _ in range(10):
            p1.take_card(Card.random())
        print(p1)

def main():
    PlayerTest()

if __name__ == '__main__':
    main()
