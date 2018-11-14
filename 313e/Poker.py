#-------------------------------------------------------------------------------
#  File: Poker.py

#  Description: play a game of poker

#  Student's Name: Terry Woodard

#  Student's UT EID: tgw466

#  Partner's Name: Jerry Che

#  Partner's UT EID: jc78222

#  Course Name: CS 313E

#  Unique Number: 86325

#  Date Created: 6/23/2018

#  Date Last Modified: 6/25/2018
#-------------------------------------------------------------------------------

import random

class Card (object):
    RANKS = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    SUITS = ('C', 'D', 'H', 'S')

    def __init__(self, rank = 12, suit = 'S'):
        if rank in Card.RANKS:
            self.rank = rank
        else:
            self.rank = 12

        if suit in Card.SUITS:
            self.suit = suit
        else:
            self.suit = 'S'

    def __str__(self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = self.rank

        return str(rank) + self.suit

    def __eq__ (self, other):
        return (self.rank == other.rank)

    def __ne__ (self, other):
        return (self.rank != other.rank)

    def __lt__ (self, other):
        return (self.rank < other.rank)

    def __le__ (self, other):
        return (self.rank <= other.rank)

    def __gt__ (self, other):
        return (self.rank > other.rank)

    def __ge__ (self, other):
        return (self.rank >= other.rank)

class Deck (object):
    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank,suit)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)

class Poker (object):
    def __init__(self, num_players, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCard_in_Hand = num_cards

        for i in range(num_players):
            hand = []
            for j in range(self.numCard_in_Hand):
                hand.append(self.deck.deal())
            self.all_hands.append(hand)

    def play(self):
        for i in range(len(self.all_hands)):
            sorted_hand = sorted(self.all_hands[i], reverse = True)
            hand = ''
            for card in sorted_hand:
                hand = hand + str(card) + ' '
            print 'Player' + str(i+1) + ': ' + hand

        #determine each type of hand and print
        points_hand = [] #create list to store points for each hand
        h = 0
        print_str =''
        for i in range (len(self.all_hands)):
            total_points = 0
            c1 = self.all_hands[i][0].rank
            c2 = self.all_hands[i][1].rank
            c3 = self.all_hands[i][2].rank
            c4 = self.all_hands[i][3].rank
            c5 = self.all_hands[i][4].rank

            if(self.is_royal(self.all_hands[i])):
                h = 10
                print_str = "Royal Flush"
            elif(self.is_straight_flush(self.all_hands[i])):
                h = 9
                print_str = "Straight Flush"
            elif(self.is_four_kind(self.all_hands[i])):
                h = 8
                print_str = "Four of a Kind"

                position = []
                pos_list = [0,1,2,3,4]

                for k in range (len(self.all_hands[i])-3):
                    if(self.all_hands[i][k].rank == self.all_hands[i][k+1].rank and self.all_hands[i][k].rank == self.all_hands[k+2].rank and self.all_hands[i][k] == self.all_hands[i][k+3]):
                        postion.append(k)
                        position.append(k+1)
                        position.append(k+2)
                        position.append(k+3)

                c1 = self.all_hands[i][position[0]].rank
                pos_list.remove(position[0])
                c2 = self.all_hands[i][position[1]].rank
                pos_list.remove(position[1])
                c3 = self.all_hands[i][position[2]].rank
                pos_list.remove(position[2])
                c4 = self.all_hands[i][position[3]].rank
                pos_list.remove(position[3])
                c5 = self.all_hands[i][pos_list[0]].rank


            elif(self.is_full_house(self.all_hands[i])):
                h = 7
                print_str = "Full House"

                three_position = []
                pair_position =[]
                pos_list = [0,1,2,3,4]


                for k in range (len(self.all_hands[i])-2):
                    if(self.all_hands[i][k].rank == self.all_hands[i][k+1].rank and self.all_hands[i][k].rank == self.all_hands[i][k+2].rank):
                        three_position.append(k)
                        three_postion.append(k+1)
                        three_position.append(k+2)

                for h in range(len(self.all_hands[i]) - 1):
                    if(self.all_hands[i][h] == self.all_hands[i][h+1]):
                        position.append(h)
                        position.append(h+1)

                c1 = self.all_hands[i][three_position[0]].rank
                c2 = self.all_hands[i][three_position[1]].rank
                c3 = self.all_hands[i][three_position[2]].rank
                c4 = self.all_hands[i][pair_position[0]].rank
                c5 = self.all_hands[i][pair_position[1]].rank


            elif(self.is_flush(self.all_hands[i])):
                h = 6
                print_str = "Flush"
            elif(self.is_straight(self.all_hands[i])):
                h = 5
                print_str = "Straight"
            elif(self.is_three_kind(self.all_hands[i])):
                h = 4
                print_str ="Three of a Kind"

                position = []
                pos_list = [0,1,2,3,4]

                for k in range (len(self.all_hands[i])-2):
                    if(self.all_hands[i][k].rank == self.all_hands[i][k+1].rank and self.all_hands[i][k].rank == self.all_hands[i][k+2].rank):
                        position.append(k)
                        position.append(k+1)
                        position.append(k+2)

                c1 = self.all_hands[i][position[0]].rank
                pos_list.remove(position[0])
                c2 = self.all_hands[i][position[1]].rank
                pos_list.remove(position[1])
                c3 = self.all_hands[i][position[2]].rank
                pos_list.remove(position[2])
                c4 = self.all_hands[i][pos_list[0]].rank
                c5 = self.all_hands[i][pos_list[1]].rank


            elif(self.is_two_pair(self.all_hands[i])):
                h = 3
                print_str = "Two Pair"

                position = []
                pos_list = [0,1,2,3,4]
                for k in range(len(self.all_hands[i]) - 1):
                    if(self.all_hands[i][k] == self.all_hands[i][k+1]):
                        position.append(k)
                        position.append(k+1)
                c1 = self.all_hands[i][position[0]].rank
                pos_list.remove(position[0])
                c2 = self.all_hands[i][position[1]].rank
                pos_list.remove(position[1])
                c3 = self.all_hands[i][position[2]].rank
                pos_list.remove(position[2])
                c4 = self.all_hands[i][position[3]].rank
                pos_list.remove(position[3])
                c5 = self.all_hands[i][pos_list[0]].rank

            elif(self.is_one_pair(self.all_hands[i])):
                h = 2
                print_str = "Pair"
                pos_list = [0,1,2,3,4]
                position = []

                for k in range(len(self.all_hands[i]) - 1):
                    if(self.all_hands[i][k] == self.all_hands[i][k+1]):
                        position.append(k)
                        position.append(k+1)

                c1 = self.all_hands[i][position[0]].rank
                pos_list.remove(position[0])
                c2 = self.all_hands[i][position[1]].rank
                pos_list.remove(position[1])
                c3 = self.all_hands[i][pos_list[0]].rank
                c4 = self.all_hands[i][pos_list[1]].rank
                c5 = self.all_hands[i][pos_list[2]].rank

            elif(self.is_high_card(self.all_hands[i])):
                h = 1
                print_str = "High Card"
                print('Player ' + str(i+1) + ": " + print_str)

                total_points = (h * (14**5)) + (c1 * (14**4)) + (c2* (14**3)) + (c3* (14**2)) + (c4* (14**1)) + c5
                points_hand.append(total_points)

        #determine winner and print
        winner = 0
        max_num = points_hand[0]
        for j in range (len(points_hand)):
            if(max_num < points_hand[j]):
                max_num = points_hand[j]
                winner = j
        print("Player",str(winner+1), "wins")




    # determine if a hand is a royal flush
    # takes as argument a list of 5 card objects and returns a boolean
    def is_royal (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i+1].suit)

        if (not same_suit):
            return False

        rank_order = True
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        return (same_suit and rank_order)


    def is_straight_flush (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return False

        rank_order = True
        for i in range (len(hand)-1):
            rank_order = rank_order and ((hand[i].rank + 1) == hand[i+1].rank)

        return (same_suit and rank_order)

    def is_four_kind (self, hand):
        same_rank = True
        for i in range(len(hand)-1):
            same_rank = same_rank and hand[i].rank == hand[i+1].rank and hand[i].rank == hand[i+2].rank and hand[i].rank == hand[i+3].rank

        return same_rank

    def is_full_house (self, hand):
        full_house = False
        if (hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank) and (hand[0].suit != hand[3].suit):
            full_house = True
        elif (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank and hand[2].rank == hand[4].rank) and (hand[0].suit != hand[3].suit):
            full_house = True

        return full_house

    def is_flush (self, hand):
        same_suit = True
        for i in range (len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return False

        return same_suit

    def is_straight (self, hand):
        rank_order = True
        for i in range (len(hand)-1):
            rank_order = rank_order and ((hand[i].rank + 1) == hand[i+1].rank)

        return rank_order

    def is_three_kind (self, hand):
        same_rank = True
        for i in range(len(hand)-1):
            same_rank = same_rank and hand[i].rank == hand[i+1].rank and hand[i].rank == hand[i+2].rank

        return same_rank

    def is_two_pair (self, hand):
        pairs = []
        for i in range(len(hand)-1):
            if (hand[i] not in pairs) and (hand[i].rank == hand[i+1].rank):
                pairs.append(hand[i].rank)

        if len(pairs) == 2:
            return True
        return False

    def is_one_pair (self, hand):
        for i in range (len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                return True
        return False


    def is_high_card (self, hand):
        if self.is_royal(hand) == True:
            return False
        elif self.is_straight_flush(hand) == True:
            return False
        elif self.is_four_kind(hand) == True:
            return False
        elif self.is_full_house(hand) == True:
            return False
        elif self.is_flush(hand) == True:
            return False
        elif self.is_straight(hand) == True:
            return False
        elif self.is_three_kind(hand) == True:
            return False
        elif self.is_two_pair(hand) == True:
            return False
        elif self.is_one_pair(hand) == True:
            return False
        else:
            return True

def main():
  # prompt user to enter the number of players
  num_players = int(raw_input('Enter number of players: '))
  while (num_players < 2) or (num_players > 6):
    num_players = int(raw_input('Enter number of players: '))

  # create the Poker object
  game = Poker(num_players)

  # play the game (poker)
  game.play()

if __name__ == "__main__":
  main()
