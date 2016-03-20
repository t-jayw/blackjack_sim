# blackjacky.py
import random

H = 'hit'
S = 'stand'
D = 'double'
Sp = 'split'

player_logic_soft_totals = {
    '21': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    '20': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    '19': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    '18': {'2':H,'3':D,'4':D,'5':D,'6':D,'7':H,'8':H,'9':H,'10':H,'A':H},
    '17': {'2':H,'3':D,'4':D,'5':D,'6':D,'7':H,'8':H,'9':H,'10':H,'A':H},
    '16': {'2':H,'3':H,'4':D,'5':D,'6':D,'7':H,'8':H,'9':H,'10':H,'A':H},
    '15': {'2':H,'3':H,'4':D,'5':D,'6':D,'7':H,'8':H,'9':H,'10':H,'A':H},
    '14': {'2':H,'3':H,'4':H,'5':D,'6':D,'7':H,'8':H,'9':H,'10':H,'A':H},
    '13': {'2':H,'3':H,'4':H,'5':H,'6':D,'7':H,'8':H,'9':H,'10':H,'A':H}
}

player_logic_split = {
    'A': {'2':Sp,'3':Sp,'4':Sp,'5':Sp,'6':Sp,'7':Sp,'8':Sp,'9':Sp,'10':Sp,'A':Sp},
    'K': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    'Q': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    'J': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    '10': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    '9': {'2':Sp,'3':Sp,'4':Sp,'5':Sp,'6':Sp,'7':H,'8':Sp,'9':Sp,'10':H,'A':H},
    '8': {'2':Sp,'3':Sp,'4':Sp,'5':Sp,'6':Sp,'7':Sp,'8':Sp,'9':Sp,'10':Sp,'A':Sp},
    '7': {'2':Sp,'3':Sp,'4':Sp,'5':Sp,'6':Sp,'7':Sp,'8':H,'9':H,'10':H,'A':H},
    '6': {'2':Sp,'3':Sp,'4':Sp,'5':Sp,'6':Sp,'7':H,'8':H,'9':H,'10':H,'A':H},
    '5': {'2':H,'3':H,'4':H,'5':H,'6':H,'7':H,'8':H,'9':H,'10':H,'A':H},
    '4': {'2':H,'3':H,'4':Sp,'5':Sp,'6':Sp,'7':H,'8':H,'9':H,'10':H,'A':H},
    '3': {'2':Sp,'3':Sp,'4':Sp,'5':Sp,'6':Sp,'7':Sp,'8':H,'9':H,'10':H,'A':H},
    '2': {'2':Sp,'3':Sp,'4':Sp,'5':Sp,'6':Sp,'7':Sp,'8':H,'9':H,'10':H,'A':H}
}

player_logic_hard_totals = {
    '21': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    '20': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    '19': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    '18': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    '17': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':S,'8':S,'9':S,'10':S,'A':S},
    '16': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':H,'8':H,'9':H,'10':H,'A':H},
    '15': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':H,'8':H,'9':H,'10':H,'A':H},
    '14': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':H,'8':H,'9':H,'10':H,'A':H},
    '13': {'2':S,'3':S,'4':S,'5':S,'6':S,'7':H,'8':H,'9':H,'10':H,'A':H},
    '12': {'2':H,'3':H,'4':S,'5':S,'6':S,'7':H,'8':H,'9':H,'10':H,'A':H},
    '11': {'2':D,'3':D,'4':D,'5':D,'6':D,'7':D,'8':D,'9':D,'10':D,'A':H},
    '10': {'2':D,'3':D,'4':D,'5':D,'6':D,'7':D,'8':D,'9':D,'10':H,'A':H},
    '9': {'2':H,'3':D,'4':D,'5':D,'6':D,'7':H,'8':H,'9':H,'10':H,'A':H},
    '8': {'2':H,'3':H,'4':H,'5':H,'6':H,'7':H,'8':H,'9':H,'10':H,'A':H},
    '7': {'2':Sp,'3':Sp,'4':Sp,'5':Sp,'6':Sp,'7':Sp,'8':H,'9':H,'10':H,'A':H},
    '6': {'2':Sp,'3':Sp,'4':Sp,'5':Sp,'6':Sp,'7':H,'8':H,'9':H,'10':H,'A':H},
    '5': {'2':H,'3':H,'4':H,'5':H,'6':H,'7':H,'8':H,'9':H,'10':H,'A':H}
}
CARD_VALS = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']


class Card:
    face_vals = {'J':10,'Q':10,'K':10,'A':1}
    def __init__(self, card):
        self.value = self.parse_card(card)
        self.card = card

    def parse_card(self, card):
        try:
            x = int(card)
        except ValueError:
            x = self.face_vals[card]
        return x

    def show_card(self): 
        print self.card, self.value

class Shoe:
    card_array = []
    def __init__(self, decks):
        self.decks = decks
        self.card_array = [Card(x) for x in (CARD_VALS * 4 * self.decks)]
        self.new_shoe = False
    
    def shuffle(self): random.shuffle(self.card_array)

    def deal_one(self, verbose = False): 
        card = self.card_array.pop()
        if card != 'CUT':
            return card
        else:
            self.new_shoe = True
            return self.card_array.pop()

    def insert_cut_card(x=20,y=40):
        place = random.randint(x,y)
        self.card_array.insert(place, 'CUT') 

class Player:
    self_strategy = None
    def __init__(self, name, money=1000):
        self.name = name
        self.money = money 
        self.bet = 5 
        self.hand = Hand([], self.bet)
        self.split_hand = Hand([], self.bet)


    def show_stats(self):
        print "name: %s"%(self.name)
        print "money: %i"%(self.money)
        print "hand:"
        for x in self.hand.card_array:
            print x.card

    def make_bet(self, hand, x=5):
        self.bet = x
        self.hand.bet = x

    def decide_play(self, hand, dealer):
        num_cards = len(hand.card_array)
        has_ace = hand.has_ace
        dealer_up = str(dealer.hand.card_array[1].value)
        decision = None
        pair = (hand.card_array[0].card if (num_cards == 2) & 
                                    (hand.card_array[0].card == hand.card_array[1].card)
                                    else False)

        if hand.soft_value > 0:
            print "looking up soft value"
            try:
                decision = player_logic_soft_totals[str(hand.soft_value)][dealer_up]
            except KeyError:
                print "soft look up failed %s %s"%(str(hand.soft_value), dealer_up )
        elif pair:
            print "looking up split rules"
            try:
                decision = player_logic_split[str(pair)][dealer_up]
            except KeyError:
                print "split look up failed %s %s"%(str(pair), dealer_up )

        else:
            print "looking up hard value %s"%(hand.hard_value)
            try:
                decision = player_logic_hard_totals[str(hand.hard_value)][dealer_up]
            except KeyError:
                print "hard look up failed %s %s"%(str(hand.hard_value), dealer_up)

        print "PLAYER DECIDES TO %s "%(decision)
        return decision

    def split(self):
        player.hand = Hand([player.hand.card_array[0]], self.bet)
        player.split_hand = Hand([player.hand.card_array[1]], self.bet)

class Dealer:
    def __init__(self):
        self.hand = Hand([], None)

class Game:
    def __init__(self, dealer, players, shoe):
        self.dealer = dealer
        self.players = players 
        self.shoe = shoe

    def deal_dealer(self, dealer):
        new_card = self.shoe.deal_one()
        dealer.hand.accept_new_card(new_card)
        #TODO don't show dealer down card
        print "DEALER CARD DEALT %s"%(new_card.card)


    def deal_player(self, hand):
        new_card = self.shoe.deal_one()
        hand.accept_new_card(new_card)
        print "PLAYER CARD DEALT %s"%(new_card.card)

    
    def start_hand(self):
        count = 0
        while count < 2:
            self.deal_dealer(self.dealer)
            for p in self.players:
                self.deal_player(p.hand)
            count += 1

    def play_hand(self, player, hand):
        if not(hand.bust or hand.blackjack):
            d = player.decide_play(hand, self.dealer)
            if d == H:
                self.deal_player(hand)
                self.play_hand(player, hand)
            elif d == S:
                print "%s stands with \n"%(player.name)
                print ' '.join([str(x.card) for x in hand.card_array])
            elif d == D:
                hand.set_bet(hand.bet * 2)
                print "%s has doubled on %s"%(player.name,
                            ' '.join([str(x.card) for x in hand.card_array]))
                self.deal_player(hand)
            elif d == Sp: 
                player.split()
                hand = player.hand,
                split_hand = player.split_hand
                self.play_hand(player, hand)
                self.play_hand(player, split_hand)
        elif hand.bust:
            print 'player bust with %s'%(' '.join([str(x.card) for x in player.hand.card_array]))
        elif hand.blackjack:
            print 'player blackjack'

    def play_dealer(self, dealer):
        if not (dealer.hand.blackjack or dealer.hand.bust) :
            if dealer.hand.has_ace & (dealer.hand.soft_value <= 17):
                self.deal_dealer(self.dealer)
                self.play_dealer(dealer)
            elif (not dealer.hand.has_ace) & (dealer.hand.hard_value < 17):
                self.deal_dealer(self.dealer)
                self.play_dealer(dealer)
        else:
            if dealer.hand.blackjack:
                print 'dealer blackjack'
            elif dealer.hand.bust:
                print 'dealer bust'   

class Hand:
    def __init__(self, card_array, bet):
        self.card_array = card_array # This array should hold Card objects
        self.has_ace = False
        self.soft_value = 0
        self.hard_value = 0
        self.bust = False
        self.blackjack = False
        self.bet = bet

    def set_bet(self, bet):
        print "Current bet %s"%(self.bet)
        self.bet = bet 
        print "NEW BET %s"%(self.bet)

    def set_has_ace(self, card_array):
        for x in card_array:
            if x.card == 'A':
                self.has_ace = True

    def accept_new_card(self, card): 
        self.card_array.append(card)
        self.compute_score()

    def compute_score(self, card_array = None):
        if card_array is None:
            card_array = self.card_array

        self.set_has_ace(self.card_array)

        self.hard_value = sum(x.value for x in card_array)

        if (self.hard_value <= 11) & self.has_ace:
            if self.hard_value + 10 > 21:
                self.soft_value = 0
            else:
                self.soft_value = self.hard_value + 10

        if len(self.card_array) == 2 and self.soft_value == 21:
            x = [card.card for card in self.card_array]
            if '10' not in x: 
                self.blackjack = True

        if self.hard_value > 21:
            self.bust = True





foo = Shoe(8)
foo.shuffle()
tyler = Player('tyler')
d = Dealer()
bar = Game(d, [tyler], foo)
bar.start_hand()
for x in bar.players:
    bar.play_hand(x, x.hand)
bar.play_dealer(bar.dealer)

p = bar.players[0]
d = bar.dealer 


def strategy_look_up(player, hand, dealer):
    num_cards = len(hand.card_array)
    has_ace = hand.has_ace
    dealer_up = dealer.hand.card_array[1]
    decision = None
    pair = (hand.card_array[0].card if (num_cards == 2) & 
                                (hand.card_array[0].card == hand.card_array[1].card)
                                else False)

    if hand.soft_value > 0:
        try:
            decision = player_logic_soft_totals[str(hand.soft_value), dealer_up]
        except KeyError:
            print "soft look up failed %s %s"%(str(hand.soft_value), dealer_up )
    elif pair:
        try:
            decision = player_logic_split[str(pair), dealer_up]
        except KeyError:
            print "split look up failed %s %s"%(str(pair), dealer_up )

    else:
        try:
            player_logic_hard_totals[str(hand.hard_value), dealer_up]
        except KeyError:
            print "hard look up failed %s %s"%(str(hand.hard_value), dealer_up)

    if num_cards > 2 & (decision == D):
        decision = H

    return decision






