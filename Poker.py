import random
class poker:
    def __init__(self) -> None:
        self.player_hands={}
        self.Cards={"A-Hearts":1,"2-Hearts":1,"3-Hearts":1,"4-Hearts":1,"5-Hearts":1,"6-Hearts":1,"7-Hearts":1,"8-Hearts":1,"9-Hearts":1,"10-Hearts":1,"J-Hearts":1,"Q-Hearts":1,"K-Hearts":1,"A-Spades":1,"2-Spades":1,"3-Spades":1,"4-Spades":1,"5-Spades":1,"6-Spades":1,"7-Spades":1,"8-Spades":1,"9-Spades":1,"10-Spades":1,"J-Spades":1,"Q-Spades":1,"K-Spades":1,"A-Diamonds":1,"2-Diamonds":1,"3-Diamonds":1,"4-Diamonds":1,"5-Diamonds":1,"6-Diamonds":1,"7-Diamonds":1,"8-Diamonds":1,"9-Diamonds":1,"10-Diamonds":1,"J-Diamonds":1,"Q-Diamonds":1,"K-Diamonds":1,"A-Clubs":1,"2-Clubs":1,"3-Clubs":1,"4-Clubs":1,"5-Clubs":1,"6-Clubs":1,"7-Clubs":1,"8-Clubs":1,"9-Clubs":1,"10-Clubs":1,"J-Clubs":1,"Q-Clubs":1,"K-Clubs":1}
        self.board=[]
        self.discard=[]
        self.total_players_with_pairs=0
        self.total_players_with_trips=0
        self.total_players_with_straights=0
        self.total_players_with_flush=0
        self.total_players_with_full_house=0
        self.total_players_with_four_of_a_kind=0
        self.total_players_with_straight_flush=0
        self.total_players_with_royal_flush=0
    def two_card_hands(self,num_of_players):
        player_number=0
        if num_of_players>22:
            print("Too many players")
            return
        for num in self.Cards:
            while len(self.player_hands)<num_of_players:
                player_number+=1
                card1=random.choice(list(self.Cards.keys()))
                card2=random.choice(list(self.Cards.keys()))
                if self.Cards[card1]==0:
                    while self.Cards[card1]==0:         
                        card1=random.choice(list(self.Cards.keys()))
                if self.Cards[card1]>0:
                    self.Cards[card1]-=1
                    self.player_hands["Player" + str(player_number)+ "'s hand"]=[card1]
                if self.Cards[card2]==0:
                    while self.Cards[card2]==0:
                        card2=random.choice(list(self.Cards.keys()))                  
                if self.Cards[card2]>0:
                    self.Cards[card2]-=1
                    self.player_hands["Player" + str(player_number)+"'s hand"]+=[card2]
            for i in self.player_hands:
                print(i, ":", self.player_hands[i])
            return
    def flop_board(self):
        discarded_cards=random.choice(list(self.Cards.keys()))
        if self.Cards[discarded_cards]==0:
            while self.Cards[discarded_cards]==0:         
                discarded_cards=random.choice(list(self.Cards.keys()))
        if self.Cards[discarded_cards]>0:
            self.Cards[discarded_cards]-=1
            self.discard+=[discarded_cards]
        flop=random.choice(list(self.Cards.keys()))
        for flips in range(3):
            if self.Cards[flop]==0:
                while self.Cards[flop]==0:         
                    flop=random.choice(list(self.Cards.keys()))
            if self.Cards[flop]>0:
                self.Cards[flop]-=1
                self.board+=[flop]
                print(flop)
    def turn(self):
        discarded_cards=random.choice(list(self.Cards.keys()))
        if self.Cards[discarded_cards]==0:
            while self.Cards[discarded_cards]==0:         
                discarded_cards=random.choice(list(self.Cards.keys()))
        if self.Cards[discarded_cards]>0:
            self.Cards[discarded_cards]-=1
            self.discard+=[discarded_cards]
        turn=random.choice(list(self.Cards.keys()))
        if self.Cards[turn]==0:
            while self.Cards[turn]==0:         
                turn=random.choice(list(self.Cards.keys()))
        if self.Cards[turn]>0:
            self.Cards[turn]-=1
            self.board+=[turn]
            print(turn)
    def river(self):
        discarded_cards=random.choice(list(self.Cards.keys()))
        if self.Cards[discarded_cards]==0:
            while self.Cards[discarded_cards]==0:         
                discarded_cards=random.choice(list(self.Cards.keys()))
        if self.Cards[discarded_cards]>0:
            self.Cards[discarded_cards]-=1
            self.discard+=[discarded_cards]
        river=random.choice(list(self.Cards.keys()))
        if self.Cards[river]==0:
            while self.Cards[river]==0:         
                river=random.choice(list(self.Cards.keys()))
        if self.Cards[river]>0:
            self.Cards[river]-=1
            self.board+=[river]
            print(river)
    ###
    ###
    # ` Hand Rankings Calculator(Type of Hands); Need to edit to determine winner/split winner
    ###
    ###
    def Royal_Flush(self):
        print("hello")
    def Straight_Flush(self):
        pass
    def Four_of_a_Kind(self):# need to edit to display high card, need to hit a test case that checks if this funtion is running properly
        if self.total_players_with_royal_flush==0 and self.total_players_with_straight_flush==0:
            all_hands=[]
            for hands in self.player_hands:
                freq_count_per_player={}
                player_hand_board_layout=self.player_hands[hands]+self.board
                for card in player_hand_board_layout:# pair, trips, and quad checker
                    if card[0] not in freq_count_per_player and (card[1]!="0"):
                        freq_count_per_player[card[0]]=1
                    elif card[:2] not in freq_count_per_player and card[1]=="0":
                        freq_count_per_player[card[:2]]=1
                    elif card[:2] in freq_count_per_player:
                        freq_count_per_player[card[:2]]+=1
                    else:
                        freq_count_per_player[card[0]]+=1
                all_hands+=[freq_count_per_player]
            for player in range(len(all_hands)):
                for cards in all_hands[player]:
                    if all_hands[player][cards]==4:
                        print("Player" + str(player)+ " " + "has quads of" + " " + str(cards))
                        self.total_players_with_four_of_a_kind+=1
    def Full_House(self):
        if self.total_players_with_royal_flush==0 and self.total_players_with_four_of_a_kind==0 and self.total_players_with_straight_flush==0:
            all_hands=[]
            trips_counter={}
            for hands in self.player_hands:
                freq_count_per_player={}
                specific_trips={}
                player_hand_board_layout=self.player_hands[hands]+self.board
                for card in player_hand_board_layout:# pair, trips, and quad checker
                    if card[0] not in freq_count_per_player and (card[1]!="0"):
                        freq_count_per_player[card[0]]=1
                    elif card[:2] not in freq_count_per_player and card[1]=="0":
                        freq_count_per_player[card[:2]]=1
                    elif card[:2] in freq_count_per_player:
                        freq_count_per_player[card[:2]]+=1
                    else:
                        freq_count_per_player[card[0]]+=1
                all_hands+=[freq_count_per_player]
            for player_number in range(len(all_hands)):
                for cards in all_hands[player_number]:
                    if all_hands[player_number][cards]==3 and player_number+1 not in trips_counter:
                        trips_counter[player_number+1]=1
                        specific_trips[player_number+1]=[cards]
            ###
            #checking for pairs for full house with 1 trips and 1 pair
            ###
            all_hands_for_pair_checker=[]
            pair_counter={}
            for hands in self.player_hands:
                freq_count_per_player_for_pairs={}
                specific_pair={}
                player_hand_board_layout_for_pairs=self.player_hands[hands]+self.board
                for card in player_hand_board_layout_for_pairs:# pair, trips, and quad checker
                    if card[0] not in freq_count_per_player_for_pairs and (card[1]!="0"):
                        freq_count_per_player_for_pairs[card[0]]=1
                    elif card[:2] not in freq_count_per_player_for_pairs and card[1]=="0":
                        freq_count_per_player_for_pairs[card[:2]]=1
                    elif card[:2] in freq_count_per_player_for_pairs:
                        freq_count_per_player_for_pairs[card[:2]]+=1
                    else:
                        freq_count_per_player_for_pairs[card[0]]+=1
                all_hands_for_pair_checker+=[freq_count_per_player_for_pairs]
            for player_number in range(len(all_hands_for_pair_checker)):
                for cards in all_hands_for_pair_checker[player_number]:
                    if all_hands_for_pair_checker[player_number][cards]==2 and player_number+1 not in pair_counter:
                        pair_counter[player_number+1]=1
                        specific_pair[player_number+1]=[cards]
                    elif all_hands_for_pair_checker[player_number][cards]==2 and player_number+1 in pair_counter:
                        pair_counter[player_number+1]+=1
                        specific_pair[player_number+1]+=[cards]
            for player in specific_trips:
                if len(specific_trips[player])==2:
                    if "10" in specific_trips[player] and "A" not in specific_trips[player] and "K" not in specific_trips[player] and "Q" not in specific_trips[player] and "J" not in specific_trips[player]:
                        for other_card in specific_trips[player] and other_card!="10":
                            othercard=other_card
                            print("\nPlayer" + str(player) + " " + "has a full house of" + " " + "10 full of" + " " + str(othercard))
                    else:
                        print("\nPlayer" + str(player) + " " + "has a full house of" + " " + str(sorted(specific_trips[player])[1]) + " " + "full of" + " " + str(sorted(specific_trips[player])[0]))
                    self.total_players_with_full_house+=1
                elif len(specific_trips[player])==1:
                    if player in specific_pair:
                        if len(specific_pair[player])==2 or (len(specific_pair[player])==1 and (specific_pair[player][0] not in specific_trips[player])) :
                            for card in specific_pair[player]:
                                if card not in specific_trips[player]:
                                    pair=card
                            for card in specific_trips[player]:
                                trips=card
                            print("\nPlayer" + str(player) + " " + "has a full house of" + " " + str(trips) + " " + "full of" + " " + str(pair))
                            self.total_players_with_full_house+=1
    def Flush(self):#need to edit to display highest flush card
        if self.total_players_with_royal_flush==0 and self.total_players_with_four_of_a_kind==0 and self.total_players_with_straight_flush==0 and self.total_players_with_full_house==0:
            all_hands_suits=[]
            for hands in self.player_hands:
                freq_count_per_player={}
                player_hand_board_layout=self.player_hands[hands]+self.board
                for card in player_hand_board_layout:# pair, trips, and quad checker
                    if card[2:] not in freq_count_per_player and (card[1]!="0"):
                        freq_count_per_player[card[2:]]=1
                    elif card[3:] not in freq_count_per_player and card[1]=="0":
                        freq_count_per_player[card[3:]]=1
                    elif card[3:] in freq_count_per_player and card[1]=="0":
                        freq_count_per_player[card[3:]]+=1
                    else:
                        freq_count_per_player[card[2:]]+=1
                all_hands_suits+=[freq_count_per_player]
            for player in range(len(all_hands_suits)):
                for suit in all_hands_suits[player]:
                    if all_hands_suits[player][suit]==5:
                        print("Player" + str(player +1) + " " + "has a flush of" + " " + str(suit))
                        self.total_players_with_flush+=1
                        break             
    def Straight(self):
        if self.total_players_with_royal_flush==0 and self.total_players_with_four_of_a_kind==0 and self.total_players_with_straight_flush==0 and self.total_players_with_flush==0 and self.total_players_with_full_house==0:
            all_hands=[]
            all_players_unique_cards=[]
            for hands in self.player_hands:
                freq_count_per_player={}
                player_hand_board_layout=self.player_hands[hands]+self.board
                for card in player_hand_board_layout:# pair, trips, and quad checker
                    if card[0] not in freq_count_per_player and (card[1]!="0"):
                        freq_count_per_player[card[0]]=1
                    elif card[:2] not in freq_count_per_player and card[1]=="0":
                        freq_count_per_player[card[:2]]=1
                    elif card[:2] in freq_count_per_player:
                        freq_count_per_player[card[:2]]+=1
                    else:
                        freq_count_per_player[card[0]]+=1
                all_hands+=[freq_count_per_player]
            for player_number in range(len(all_hands)):
                solo_unique_cards_per_player=[]
                for card_number in all_hands[player_number]:
                    solo_unique_cards_per_player+=[card_number]
                all_players_unique_cards+=[solo_unique_cards_per_player]
            for player in range(len(all_players_unique_cards)):
                if "10" in all_players_unique_cards[player] and "J" in all_players_unique_cards[player] and "Q" in all_players_unique_cards[player] and "K" in all_players_unique_cards[player] and "A" in all_players_unique_cards[player]:
                    print("Player" + str(player+1) + " " + "has a straight of 10, J, Q, K, A")
                    self.total_players_with_straights+=1
                elif "10" in all_players_unique_cards[player] and "J" in all_players_unique_cards[player] and "Q" in all_players_unique_cards[player] and "K" in all_players_unique_cards[player] and "9" in all_players_unique_cards[player]:
                    print("Player" + str(player+1) + " " + "has a straight of 9, 10, J, Q, K")
                    self.total_players_with_straights+=1
                elif "10" in all_players_unique_cards[player] and "J" in all_players_unique_cards[player] and "Q" in all_players_unique_cards[player] and "8" in all_players_unique_cards[player] and "9" in all_players_unique_cards[player]:
                    print("Player" + str(player+1) + " " + "has a straight of 8, 9, 10, J, Q")
                    self.total_players_with_straights+=1
                elif "10" in all_players_unique_cards[player] and "J" in all_players_unique_cards[player] and "7" in all_players_unique_cards[player] and "8" in all_players_unique_cards[player] and "9" in all_players_unique_cards[player]:
                    print("Player" + str(player+1) + " " + "has a straight of 7, 8, 9, 10, J")
                    self.total_players_with_straights+=1
                elif "10" in all_players_unique_cards[player] and "6" in all_players_unique_cards[player] and "7" in all_players_unique_cards[player] and "8" in all_players_unique_cards[player] and "9" in all_players_unique_cards[player]:
                    print("Player" + str(player+1) + " " + "has a straight of 6, 7, 8, 9, 10")
                    self.total_players_with_straights+=1
                elif "5" in all_players_unique_cards[player] and "6" in all_players_unique_cards[player] and "7" in all_players_unique_cards[player] and "8" in all_players_unique_cards[player] and "9" in all_players_unique_cards[player]:
                    print("Player" + str(player+1) + " " + "has a straight of 5, 6, 7, 8, 9")
                    self.total_players_with_straights+=1
                elif "5" in all_players_unique_cards[player] and "6" in all_players_unique_cards[player] and "7" in all_players_unique_cards[player] and "4" in all_players_unique_cards[player] and "8" in all_players_unique_cards[player]:
                    print("Player" + str(player+1) + " " + "has a straight of 4, 5, 6, 7, 8")
                    self.total_players_with_straights+=1
                elif "5" in all_players_unique_cards[player] and "6" in all_players_unique_cards[player] and "7" in all_players_unique_cards[player] and "4" in all_players_unique_cards[player] and "3" in all_players_unique_cards[player]:
                    print("Player" + str(player+1) + " " + "has a straight of 3, 4, 5, 6, 7")
                    self.total_players_with_straights+=1
                elif "5" in all_players_unique_cards[player] and "6" in all_players_unique_cards[player] and "2" in all_players_unique_cards[player] and "4" in all_players_unique_cards[player] and "3" in all_players_unique_cards[player]:
                    print("Player" + str(player+1) + " " + "has a straight of 2, 3, 4, 5, 6")
                    self.total_players_with_straights+=1
                elif "5" in all_players_unique_cards[player] and "A" in all_players_unique_cards[player] and "2" in all_players_unique_cards[player] and "4" in all_players_unique_cards[player] and "3" in all_players_unique_cards[player]:
                    print("Player" + str(player+1) + " " + "has a straight of A, 2, 3, 4, 5")
                    self.total_players_with_straights+=1
    def Trips_checker(self):
        if self.total_players_with_royal_flush==0 and self.total_players_with_four_of_a_kind==0 and self.total_players_with_straight_flush==0 and self.total_players_with_flush==0 and self.total_players_with_full_house==0 and self.total_players_with_straights==0:
            all_hands=[]
            trips_counter={}
            for hands in self.player_hands:
                freq_count_per_player={}
                specific_trips={}
                player_hand_board_layout=self.player_hands[hands]+self.board
                for card in player_hand_board_layout:# pair, trips, and quad checker
                    if card[0] not in freq_count_per_player and (card[1]!="0"):
                        freq_count_per_player[card[0]]=1
                    elif card[:2] not in freq_count_per_player and card[1]=="0":
                        freq_count_per_player[card[:2]]=1
                    elif card[:2] in freq_count_per_player:
                        freq_count_per_player[card[:2]]+=1
                    else:
                        freq_count_per_player[card[0]]+=1
                all_hands+=[freq_count_per_player]
            for player_number in range(len(all_hands)):
                for cards in all_hands[player_number]:
                    if all_hands[player_number][cards]==3 and player_number+1 not in trips_counter:
                        trips_counter[player_number+1]=1
                        specific_trips[player_number+1]=[cards]
            for player in specific_trips:
                if len(specific_trips[player])==1:#if there are 2 trips in their hand, they'll have a full house, which will be accounted for in the full house subclass
                    print("\nPlayer" + str(player) + " " + "has trips of" + " " + str(specific_trips[player][0]))
                    self.total_players_with_trips+=1
    def Pair_and_TwoPair_Checker(self):#need to check for higher pair when two pair hits(if three pairs)
        if self.total_players_with_royal_flush==0 and self.total_players_with_trips==0 and self.total_players_with_four_of_a_kind==0 and self.total_players_with_straight_flush==0 and self.total_players_with_flush==0 and self.total_players_with_full_house==0 and self.total_players_with_straights==0:
            all_hands=[]
            pair_counter={}
            for hands in self.player_hands:
                freq_count_per_player={}
                specific_pair={}
                player_hand_board_layout=self.player_hands[hands]+self.board
                for card in player_hand_board_layout:# pair, trips, and quad checker
                    if card[0] not in freq_count_per_player and (card[1]!="0"):
                        freq_count_per_player[card[0]]=1
                    elif card[:2] not in freq_count_per_player and card[1]=="0":
                        freq_count_per_player[card[:2]]=1
                    elif card[:2] in freq_count_per_player:
                        freq_count_per_player[card[:2]]+=1
                    else:
                        freq_count_per_player[card[0]]+=1
                all_hands+=[freq_count_per_player]
            for player_number in range(len(all_hands)):
                for cards in all_hands[player_number]:
                    if all_hands[player_number][cards]==2 and player_number+1 not in pair_counter:
                        pair_counter[player_number+1]=1
                        specific_pair[player_number+1]=[cards]
                    elif all_hands[player_number][cards]==2 and player_number+1 in pair_counter:
                        pair_counter[player_number+1]+=1
                        specific_pair[player_number+1]+=[cards]
            for player in specific_pair:
                if len(specific_pair[player])==1:
                    print("\nPlayer" + str(player) + " " + "has a pair of" + " " + str(specific_pair[player][0]))
                    self.total_players_with_pairs+=1
                else:
                    print("\nPlayer" + str(player) + " " + "has a two pair of" + " " +  str(specific_pair[player][0]) + " " + "and" + " " + str(specific_pair[player][1]))   
                    self.total_players_with_pairs+=1
    def High_Card_checker(self):
        no_suit_card_hands=[]
        if self.total_players_with_four_of_a_kind==0 and self.total_players_with_full_house==0 and self.total_players_with_royal_flush==0 and self.total_players_with_flush==0 and self.total_players_with_pairs==0 and self.total_players_with_trips==0 and self.total_players_with_straights==0:#only runs if nobody has pairs
            for hands in self.player_hands:
                if self.player_hands[hands][0][1]=="0" and self.player_hands[hands][1][1]=="0":
                    no_suit_card_hands+=[["10","10"]]
                elif self.player_hands[hands][0][1]=="0" and self.player_hands[hands][1][1]!="0":
                    no_suit_card_hands+=[["10",self.player_hands[hands][1][0]]]
                elif self.player_hands[hands][0][1]!="0" and self.player_hands[hands][1][1]!="0":
                    no_suit_card_hands+=[[self.player_hands[hands][0][0],self.player_hands[hands][1][0]]]
                else:
                    no_suit_card_hands+=[[self.player_hands[hands][0][0],"10"]]
            for player_num in range(len(no_suit_card_hands)):
                if "A" in no_suit_card_hands[player_num]:
                    print("Player"+ str(player_num+1)+ " " + "has a high card of A")
                elif "K" in no_suit_card_hands[player_num]:
                    print("Player"+ str(player_num+1)+ " " + "has a high card of K")
                elif "Q" in no_suit_card_hands[player_num]:
                    print("Player"+ str(player_num+1)+ " " + "has a high card of Q")                
                elif "J" in no_suit_card_hands[player_num]:
                    print("Player"+ str(player_num+1)+ " " + "has a high card of J")
                elif "10" in no_suit_card_hands[player_num]:
                    print("Player"+ str(player_num+1)+ " " + "has a high card of 10")
                else:
                    sorted_lst=sorted(no_suit_card_hands[player_num])
                    print("Player"+ str(player_num+1)+ " " + "has a high card of" + " " + str(sorted_lst[len(sorted_lst)-1]))
    def probability(self):#calclates each players chance of winning pre-flop, flop, turn, and river
        pass




Number_of_Players=4 #Type in number of players


###
###

#invocation
print(str(Number_of_Players)+" " + "players are at the table\n\n")
poker=poker()
poker.two_card_hands(Number_of_Players)
print("\nFlop:")
poker.flop_board()
print("\nTurn")
poker.turn()
print("\nRiver:")
poker.river()
print("\nPlayers Hands:")
poker.Four_of_a_Kind()
poker.Full_House()
poker.Flush()
poker.Straight()
poker.Trips_checker()
poker.Pair_and_TwoPair_Checker()
poker.High_Card_checker()
#end invocation
###
###