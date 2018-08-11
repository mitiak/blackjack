#!/usr/bin/python3

from bj_logic import BJLogic
from deck import Deck
from dealer import Dealer
from player import Player
from time import sleep
import os

class Table():
    def __init__(self, dealer, player):
        self.dealer = dealer
        self.deck = Deck(shuffle=True)
        self.player = player
        self.round_num = 0

    def get_dealer(self):
        return self.dealer

    def get_player(self):
        return self.player

    def get_deck(self):
        return self.deck

    def draw(self):
        os.system('clear')
        print('Round', self.round_num, '- Cards left:', str(len(self.deck)))
        print(str(self.dealer) + ", Score: " +  str(BJLogic.get_player_score(self.dealer)))
        print(str(self.player) + ", Score: " +  str(BJLogic.get_player_score(self.player)))

    def round_init(self):
        self.round_num += 1
        self.dealer.throw_cards()
        self.player.throw_cards()
        self.dealer.deal_cards_from_deck(self.deck, self.dealer, 1, False)
        self.dealer.deal_cards_from_deck(self.deck, self.dealer, 1, True)
        self.dealer.deal_cards_from_deck(self.deck, self.player, 2, True)

        
class TableTest():
    def __init__(self):
        dealer = Dealer('John', 'Doe')
        player = Player('Daniel', 'Negreanu', 1000)
        self.t = Table(dealer, player)
        self.t.draw()

    def play_game(self):
        while len(self.t.get_deck()):
            self.play_round()

    def play_round(self):
        dealer = self.t.get_dealer()
        player = self.t.get_player()
        deck = self.t.get_deck()
        self.t.round_init()
        plr_score = BJLogic.get_player_score(player)
        if plr_score == 21:
            self.t.draw()
            print('Player wins')
            sleep(2)
            return
        
        while True:
            self.t.draw()
            cmd = input("Enter command [h-hit][s-stop] > ")
            if cmd == 'exit':
                print("Good bye")
                break
            if cmd == 'h':
                dealer.deal_cards_from_deck(deck, player)
                plr_score = BJLogic.get_player_score(player)
                if plr_score == 21:
                    self.t.draw()
                    print('Player wins')
                    break
                elif plr_score > 21:
                    self.t.draw()
                    print('Dealer wins')
                    break
            if cmd == 's':
                dealer.flip_card()
                dlr_score = BJLogic.get_player_score(dealer)
                plr_score = BJLogic.get_player_score(player)
                self.t.draw()
                while dlr_score < 17:
                    sleep(1)
                    dealer.deal_cards_from_deck(deck, dealer)
                    dlr_score = BJLogic.get_player_score(dealer)
                    self.t.draw()
                if dlr_score <= 21 and dlr_score > plr_score:
                    print('Dealer wins')
                elif dlr_score == plr_score:
                    print('It\'s a draw!')
                else:
                    print('Player wins')
                break
        sleep(2)



def main():
    test = TableTest()
    test.play_game()

if __name__ == '__main__':
    main()

        


