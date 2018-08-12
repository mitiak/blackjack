#!/usr/bin/python3

from bj_logic import BJLogic
from deck import Deck
from dealer import Dealer, NoCardsException
from player import Player
from time import sleep
import os

class Table():
    def __init__(self, dealer, player):
        self.dealer = dealer
        self.deck = Deck(shuffle=True)
        self.player = player
        self.round_num = 0
        self.wins = [0, 0]
        

    def get_dealer(self):
        return self.dealer

    def get_player(self):
        return self.player

    def get_deck(self):
        return self.deck

    def draw(self, sleep_time=0, message='', get_input=False):
        os.system('clear')
        print('Round', self.round_num, '- Cards left:', str(len(self.deck)), '[' + '|' * len(self.deck) + ' ' * (52-len(self.deck)) +']')
        print('[wins:' + str(self.wins[0]) + ']' + str(self.dealer) + ", Score: " +  str(BJLogic.get_player_score(self.dealer)))
        print('[wins:' + str(self.wins[1]) + ']' + str(self.player) + ", Score: " +  str(BJLogic.get_player_score(self.player)))
        print('-------------------------------------------------------------------------------')
        if get_input:
            return input("Enter command [h-hit][s-stop] > ")
        else:
            print(message)
        sleep(sleep_time)

    def round_init(self):
        self.round_num += 1
        if len(self.deck) < 4:
            raise NoCardsException('Not enough cards')
        try:
            self.dealer.deal_cards_from_deck(self.deck, self.dealer, 1, False)
            self.dealer.deal_cards_from_deck(self.deck, self.dealer, 1, True)
            self.dealer.deal_cards_from_deck(self.deck, self.player, 2, True)
        except NoCardsException as e:
            print(e)
    
    def round_fini(self, winner):
        self.dealer.throw_cards()
        self.player.throw_cards()
        if winner is None:
            return
        if winner == self.player:
            winner_idx = 1
        else:
            winner_idx = 0
        self.wins[winner_idx] += 1
        
        

    def dealer_open_card(self):
        self.dealer.flip_card()
        return BJLogic.get_player_score(self.dealer)
    
    def deal_card_to_player(self, player):
        self.dealer.deal_cards_from_deck(self.deck, player)
        return BJLogic.get_player_score(player)

    def dealer_take_cards(self):
        if self.dealer.get_deck().get_card(0).is_visible == False:
            dlr_score = self.dealer_open_card()
        else:
            self.dealer.deal_cards_from_deck(self.deck, self.dealer)
            dlr_score = BJLogic.get_player_score(self.dealer)
        return dlr_score

        
        
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
        try:
            self.t.round_init()
        except NoCardsException as e:
            self.t.draw(2, str(e))
            exit(0)
        plr_score = BJLogic.get_player_score(player)
        if plr_score == 21:
            self.t.draw(2, 'Easy!..')
            self.t.round_fini(player)
            return
        
        while True:
            cmd = self.t.draw(0, 'Enter command [h-hit][s-stop] > ', True)

            if cmd == 'exit':
                self.t.draw(2, 'Good bye')
                exit(0)

            if cmd == 'h': # hit
                try:
                    plr_score = self.t.deal_card_to_player(player)
                except NoCardsException as e:
                    self.t.draw(2, str(e))
                finally:
                    if plr_score == 21:
                        self.t.draw(2, 'Player wins')
                        self.t.round_fini(player)
                        break
                    elif plr_score > 21:
                        self.t.draw(2, 'Dealer wins')
                        self.t.round_fini(dealer)
                        break

            if cmd == 's': # stop
                while self.t.dealer_take_cards() < 17:
                    self.t.draw(1)
                dlr_score = BJLogic.get_player_score(dealer)
                if dlr_score <= 21 and dlr_score > plr_score:
                    self.t.draw(2, 'Dealer wins')
                    self.t.round_fini(dealer)
                elif dlr_score == plr_score:
                    self.t.draw(2, 'It\'s a draw!')
                    self.t.round_fini(None)
                else:
                    self.t.draw(2, 'Player wins')
                    self.t.round_fini(player)
                break

def main():
    test = TableTest()
    test.play_game()

if __name__ == '__main__':
    main()

        


