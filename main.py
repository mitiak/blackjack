#!/usr/bin/python3

import os
from time import sleep
from deck import Deck
from player import Player
from dealer import Dealer
from bj_logic import BJLogic

dlr = Dealer('John', 'Doe')
dck = Deck(shuffle=True)
plr = Player('Daniel', 'Negreanu', 1000)

def draw():
    os.system('clear')
    print(str(dlr) + ", Score: " +  str(BJLogic.get_player_score(dlr)))
    print(str(plr) + ", Score: " +  str(BJLogic.get_player_score(plr)))


def main():

    dlr.deal_cards_from_deck(dck, dlr, 1, False)
    dlr.deal_cards_from_deck(dck, dlr, 1, True)
    dlr.deal_cards_from_deck(dck, plr, 2, True)

    while True:
        draw()
        cmd = input("Enter command [h-hit][s-stop] > ")
        if cmd == 'exit':
            print("Good bye")
            return
        if cmd == 'h':
            dlr.deal_cards_from_deck(dck, plr)
            plr_score = BJLogic.get_player_score(plr)
            if plr_score == 21:
                draw()
                print('Player wins')
                return
            elif plr_score > 21:
                draw()
                print('Dealer wins')
                return
        if cmd == 's':
            dlr.flip_card()
            dlr_score = BJLogic.get_player_score(dlr)
            plr_score = BJLogic.get_player_score(plr)
            draw()
            while dlr_score < 17:
                sleep(1)
                dlr.deal_cards_from_deck(dck, dlr)
                dlr_score = BJLogic.get_player_score(dlr)
                draw()
            if dlr_score <= 21 and dlr_score > plr_score:
                print('Dealer wins')
            elif dlr_score == plr_score:
                print('It\'s a draw!')
            else:
                print('Player wins')
            return



if __name__ == '__main__':
    main()