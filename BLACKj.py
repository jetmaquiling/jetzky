import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank+" of "+self.suit

class Deck:
    def __init__(self):
        self.all_deck = []
        for suit in suits:
            for rank in ranks:
                self.all_deck.append(Card(suit,rank))
                
                
                
    def shuffle(self):
        random.shuffle(self.all_deck)

    def get_one_card(self):
        return self.all_deck.pop()




bool1 = True
while bool1:
    print("Welcome To Jumanji!")
    welcome_answer = str(input("Would You like to play? Y / N : "))
    welcome_answers = welcome_answer.upper()
    if welcome_answers == "Y":
        bool2 = True
        while bool2:
            try:
                jet = int(input("How Much Will You Bet? "))
                bet = abs(jet)
            except :
                print("You Did Not Type a Number! Please Try Again")
                continue
            else:
                if bet > 100:
                    print("You Can Only Bet within $100, Please Try Again! ")
                    continue
                else:
                    bool3 = True
                    while bool3:
                        dealers_value = 0
                        players_value = 0
                        
                        
                        print("DEALER's CARD")
                        dealer1 = Deck()
                        Deck.shuffle(dealer1)
                        dealer_one = Deck.get_one_card(dealer1)
                        dealers_value = dealer_one.value + dealers_value
                        print("CLOSED CARD")
                        dealer2 = Deck()
                        Deck.shuffle(dealer2)
                        dealer_two = Deck.get_one_card(dealer2)
                        dealers_value = dealer_two.value + dealers_value
                        print(dealer_two)
                        print(dealers_value)
                        print("\n ")
                        print("\n ")
                        print("PLAYER's CARD")
                        player1 = Deck()
                        Deck.shuffle(player1)
                        player_one = Deck.get_one_card(player1)
                        players_value = player_one.value + players_value
                        print(player_one)
                        player2 = Deck()
                        Deck.shuffle(player2)
                        player_two = Deck.get_one_card(player2)
                        players_value = player_two.value + players_value
                        print(player_two)
                        print(players_value)

                        if dealers_value == 21:

                            print(f"YOU LOST ${bet}")
                            bool2 = False
                            break
                        if players_value == 21:
                            print(f"YOU WON ${(bet/2)+bet}!!!")
                            bool2 = False
                            break

                        if dealers_value > 21:
                            print(f"Dealer BUST! You WON ${(bet/2)+bet}!!!")
                            bool2 = False
                            break

                        if players_value > 21:
                            print(f"PLAYER BUST!!! You LOST  ${bet}!!!")
                            bool2 = False
                            break

                        choice1 = input("HIT OR STAND! <H> OR <S>")
                        choice1 = choice1.upper()
                        
                        
                        
                        
                        
                        if choice1 == "H":
                            print("DEALER's CARD")
                            print("CLOSED CARD")                       
                            print(dealer_two)
                            print(dealers_value)
                            print("\n ")
                            print("\n ")
                            print("PLAYER's CARD")                            
                            print(player_one)
                            print(player_two)
                            player3 = Deck()
                            Deck.shuffle(player3)
                            player_three = Deck.get_one_card(player3)
                            players_value = player_three.value + players_value
                            print(player_three)
                            print(players_value)
                            if dealers_value == 21:
                                print(f"YOU LOST  ${bet}!!!")
                                bool2 = False
                                break
                            if players_value == 21:
                                print(f"YOU WON ${(bet/2)+bet}!!!")
                                bool2 = False
                                break
                            if players_value > 21:
                                print(f"PLAYER BUST You LOST  ${bet}!!!")
                                bool2 = False
                                break


                            choice2 = input("HIT OR STAND! <H> OR <S>: ")
                            choice2 = choice2.upper()

                            if choice2 == "H":
                                print("DEALER's CARD")
                                print("CLOSED CARD")                       
                                print(dealer_two)
                                print(dealers_value)
                                print("\n ")
                                print("\n ")
                                print("PLAYER's CARD")                            
                                print(player_one)
                                print(player_two)
                                print(player_three)
                                player4 = Deck()
                                Deck.shuffle(player4)
                                player_four = Deck.get_one_card(player4)
                                players_value = player_four.value + players_value
                                print(player_four)
                                print(players_value)
                                if dealers_value == 21:
                                    print(f"YOU LOST  ${bet}!!!")
                                    bool2 = False
                                    break
                                if players_value == 21:
                                    print(f"YOU WON ${(bet/2)+bet}!!!")
                                    bool2 = False
                                    break
                                if players_value > 21:
                                    print(f"PLAYER BUST You LOST  ${bet}!!!")
                                    bool2 = False
                                    break

                                choice3 = input("HIT OR STAND! <H> OR <S>: ")
                                choice3 = choice2.upper()

                                if choice3 == "H":
                                    print("DEALER's CARD")
                                    print("CLOSED CARD")                       
                                    print(dealer_two)
                                    print(dealers_value)
                                    print("\n ")
                                    print("\n ")
                                    print("PLAYER's CARD")                            
                                    print(player_one)
                                    print(player_two)
                                    print(player_three)
                                    print(player_four)

                                    print(players_value)
                                    if dealers_value == 21:
                                        print(f"YOU LOST  ${bet}!!!")
                                        bool2 = False
                                        break
                                    if players_value == 21:
                                        print(f"YOU WON ${(bet/2)+bet}!!!")
                                        bool2 = False
                                        break
                                    if players_value > 21:
                                        print(f"PLAYER BUST You LOST  ${bet}!!!")
                                        bool2 = False
                                        break

                                    choice4 = input("HIT OR STAND! <H> OR <S>: ")
                                    choice4 = choice4.upper()
                                    if choice4 == "H":
                                        print("DEALER's CARD")
                                        print("CLOSED CARD")                       
                                        print(dealer_two)
                                        print(dealers_value)
                                        print("\n ")
                                        print("\n ")
                                        print("PLAYER's CARD")                            
                                        print(player_one)
                                        print(player_two)
                                        print(player_three)
                                        print(player_four)
                                        print(players_value)
                                        if dealers_value == 21:
                                            print(f"YOU LOST  ${bet}!!!")
                                            bool2 = False
                                            break
                                        if players_value == 21:
                                            print(f"YOU WON ${(bet/2)+bet}!!!")
                                            bool2 = False
                                            break
                                        if players_value > 21:
                                            print(f"PLAYER BUST You LOST  ${bet}!!!")
                                            bool2 = False
                                            break
                                        choice5 = "S"
                                        bool2 = False
                                        break







                                    else: 
                                        #First
                                        print("DEALER's CARD")
                                        print(dealer_one)
                                        print(dealer_two)
                                        print(dealers_value)
                                        if dealers_value < 17:
                                            dealer3 = Deck()
                                            Deck.shuffle(dealer3)
                                            dealer_three = Deck.get_one_card(dealer3)
                                            dealers_value = dealer_three.value + dealers_value
                                            print(dealer_three)
                                        if dealers_value < 17:
                                            dealer4 = Deck()
                                            Deck.shuffle(dealer4)
                                            dealer_four = Deck.get_one_card(dealer4)
                                            dealers_value = dealer_four.value + dealers_value
                                            print(dealer_four)
                                        if dealers_value < 17:
                                            dealer5 = Deck()
                                            Deck.shuffle(dealer5)
                                            dealer_five = Deck.get_one_card(dealer5)
                                            dealers_value = dealer_five.value + dealers_value
                                            print(dealer_five)
                                        print(dealers_value)



                                            
                                        print("\n ")
                                        print("\n ")
                                        print("PLAYER's CARD")
                                        print(player_one)
                                        print(player_two)
                                        print(players_value)




                                        if dealers_value == 21:
                                            print(f"Dealer is equals to 21 YOU LOST  ${bet}!!!")
                                            bool2 = False
                                            break

                                        if players_value == 21:
                                            print(f"Player is equals to 21 YOU WON ${(bet/2)+bet}!!!")
                                            bool2 = False
                                            break

                                        if dealers_value > 21:
                                            print(f"DEALER BUST YOU WON ${(bet/2)+bet}!!!")
                                            bool2 = False
                                            break

                                        if dealers_value > players_value and dealers_value < 21:
                                            print(f"Dealer has higher Value, YOU LOST  ${bet}")
                                            bool2 = False
                                            break 

                                        if players_value > dealers_value and players_value < 21:
                                            print(f"Player has higher Value, YOU WON ${(bet/2)+bet}")
                                            bool2 = False
                                            break 

                                else:
                                    #First
                                    print("DEALER's CARD")
                                    print(dealer_one)
                                    print(dealer_two)
                                    print(dealers_value)
                                    if dealers_value < 17:
                                        dealer3 = Deck()
                                        Deck.shuffle(dealer3)
                                        dealer_three = Deck.get_one_card(dealer3)
                                        dealers_value = dealer_three.value + dealers_value
                                        print(dealer_three)
                                    if dealers_value < 17:
                                        dealer4 = Deck()
                                        Deck.shuffle(dealer4)
                                        dealer_four = Deck.get_one_card(dealer4)
                                        dealers_value = dealer_four.value + dealers_value
                                        print(dealer_four)
                                    if dealers_value < 17:
                                        dealer5 = Deck()
                                        Deck.shuffle(dealer5)
                                        dealer_five = Deck.get_one_card(dealer5)
                                        dealers_value = dealer_five.value + dealers_value
                                        print(dealer_five)
                                    print(dealers_value)



                                        
                                    print("\n ")
                                    print("\n ")
                                    print("PLAYER's CARD")
                                    print(player_one)
                                    print(player_two)
                                    print(players_value)




                                    if dealers_value == 21:
                                        print(f"Dealer is equals to 21 YOU LOST  ${bet}!!!")
                                        bool2 = False
                                        break

                                    if players_value == 21:
                                        print(f"Player is equals to 21 YOU WON ${(bet/2)+bet}!!!")
                                        bool2 = False
                                        break

                                    if dealers_value > 21:
                                        print(f"DEALER BUST YOU WON ${(bet/2)+bet}!!!")
                                        bool2 = False
                                        break

                                    if dealers_value > players_value and dealers_value < 21:
                                        print(f"Dealer has higher Value, YOU LOST  ${bet}")
                                        bool2 = False
                                        break 

                                    if players_value > dealers_value and players_value < 21:
                                        print(f"Player has higher Value, YOU WON ${(bet/2)+bet}")
                                        bool2 = False
                                        break 
                                            
                                
                            else:
                                print("DEALER's CARD")
                                print(dealer_one)
                                print(dealer_two)
                                print(dealers_value)
                                if dealers_value < 17:
                                    dealer3 = Deck()
                                    Deck.shuffle(dealer3)
                                    dealer_three = Deck.get_one_card(dealer3)
                                    dealers_value = dealer_three.value + dealers_value
                                    print(dealer_three)
                                if dealers_value < 17:
                                    dealer4 = Deck()
                                    Deck.shuffle(dealer4)
                                    dealer_four = Deck.get_one_card(dealer4)
                                    dealers_value = dealer_four.value + dealers_value
                                    print(dealer_four)
                                if dealers_value < 17:
                                    dealer5 = Deck()
                                    Deck.shuffle(dealer5)
                                    dealer_five = Deck.get_one_card(dealer5)
                                    dealers_value = dealer_five.value + dealers_value
                                    print(dealer_five)
                                print(dealers_value)



                                    
                                print("\n ")
                                print("\n ")
                                print("PLAYER's CARD")
                                print(player_one)
                                print(player_two)
                                print(players_value)




                                if dealers_value == 21:
                                    print(f"Dealer is equals to 21 YOU LOST  ${bet}!!!")
                                    bool2 = False
                                    break

                                if players_value == 21:
                                    print(f"Player is equals to 21 YOU WON ${(bet/2)+bet}!!!")
                                    bool2 = False
                                    break

                                if dealers_value > 21:
                                    print(f"DEALER BUST YOU WON ${(bet/2)+bet}!!!")
                                    bool2 = False
                                    break

                                if dealers_value > players_value and dealers_value < 21:
                                    print(f"Dealer has higher Value, YOU LOST  ${bet}")
                                    bool2 = False
                                    break 

                                if players_value > dealers_value and players_value < 21:
                                    print(f"Player has higher Value, YOU WON ${(bet/2)+bet}")
                                    bool2 = False
                                    break 
                        else:
                            #First
                            print("DEALER's CARD")
                            print(dealer_one)
                            print(dealer_two)
                            print(dealers_value)
                            if dealers_value < 17:
                                dealer3 = Deck()
                                Deck.shuffle(dealer3)
                                dealer_three = Deck.get_one_card(dealer3)
                                dealers_value = dealer_three.value + dealers_value
                                print(dealer_three)
                            if dealers_value < 17:
                                dealer4 = Deck()
                                Deck.shuffle(dealer4)
                                dealer_four = Deck.get_one_card(dealer4)
                                dealers_value = dealer_four.value + dealers_value
                                print(dealer_four)
                            if dealers_value < 17:
                                dealer5 = Deck()
                                Deck.shuffle(dealer5)
                                dealer_five = Deck.get_one_card(dealer5)
                                dealers_value = dealer_five.value + dealers_value
                                print(dealer_five)
                            print(dealers_value)



                                
                            print("\n ")
                            print("\n ")
                            print("PLAYER's CARD")
                            print(player_one)
                            print(player_two)
                            print(players_value)



                            if players_value == dealers_value:
                                print("ITS A TIE!!! PUSH!!!")
                                bool2 = False
                                break


                            if dealers_value == 21:
                                print(f"Dealer is equals to 21 YOU LOST  ${bet}!!!")
                                bool2 = False
                                break

                            if players_value == 21:
                                print(f"Player is equals to 21 YOU WON ${(bet/2)+bet}!!!")
                                bool2 = False
                                break

                            if dealers_value > 21:
                                print(f"DEALER BUST YOU WON ${(bet/2)+bet}!!!")
                                bool2 = False
                                break

                            if dealers_value > players_value and dealers_value < 21:
                                print(f"Dealer has higher Value, YOU LOST  ${bet}")
                                bool2 = False
                                break 

                            if players_value > dealers_value and players_value < 21:
                                print(f"Player has higher Value, YOU WON ${(bet/2)+bet}")
                                bool2 = False
                                break 
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        bool2 = False
                        break




    elif welcome_answer == "N":
        bool1 == False
        break
    else: 
        print("Invalid answer")
        continue