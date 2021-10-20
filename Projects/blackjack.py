from random import shuffle

suit = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
rank = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
bet_amount = 0

class Deck:
     
    def __init__(self):        
        self.deck = []
        for color in suit:
            for num in rank:
                self.deck.append(num + " of " + color)

    def shuffle(self):        
        shuffle(self.deck)

    def deal(self):        
        return self.deck.pop()

class Hand:
    
    def __init__(self):        
        self.cards = []
        self.value = 0
        self.ace_count = 0

    def add_card(self,cards):        
        self.cards.append(cards)

    def calculate_card_value(self,cards):        
        i = 0
        while(i != len(self.cards)):            
            if('Two' in self.cards[i]):
                self.value += 2
            elif('Three' in self.cards[i]):
                self.value += 3
            elif('Four' in self.cards[i]):
                self.value += 4
            elif('Five' in self.cards[i]):
                self.value += 5
            elif('Six' in self.cards[i]):
                self.value += 6
            elif('Seven' in self.cards[i]):
                self.value += 7
            elif('Eight' in self.cards[i]):
                self.value += 8
            elif('Nine' in self.cards[i]):
                self.value += 9
            elif('Ten' in self.cards[i]):
                self.value += 10
            elif('King' in self.cards[i]):
                self.value += 10
            elif('Queen' in self.cards[i]):
                self.value += 10
            elif('Jack' in self.cards[i]):
                self.value += 10
            elif('Ace' in self.cards[i]):
                self.value += 11
                self.ace_count += 1
            
            i += 1

    def ace_correction(self):
        if(self.value >21 and self.ace_count >= 1):
            self.value -= 10
            self.ace_count -= 1

    def display_player_cards(self):
        print('Your cards are : ')
        for i in range(0,len(self.cards)):
            print(self.cards[i])

    def display_dealer_cards(self):
        print('\nDealer\'s cards are : ')
        for i in range(0,(len(self.cards)-1)):
            print(self.cards[i])
        print('Hidden Card \n')

    def display_dealer_cards_win(self):
        print('\nDealer\'s cards are : ')
        for i in range(0,len(self.cards)):
            print(self.cards[i])
            
    def reset_card_value(self):
        self.value = 0

    def card_value(self):
        return self.value

class Chips:

    def __init__(self):        
        self.coins = 100

    def coin_balance(self):
        return self.coins
        
    def win_bet(self,win_amount):        
        self.coins += win_amount

    def lose_bet(self,lose_amount):        
        self.coins -= lose_amount

def action():    

    while(1):
            
        try:
            action = int(input('\nSelect your action : 1 to Hit or 2 to Stand \n'))
        except ValueError:
            print('Enter a number from 1 or 2! \n')
        
        else:
            if(action == 1):
                hit()
                player.display_player_cards()
                player.reset_card_value()
                player.calculate_card_value(player.cards)
                player.ace_correction()
                if(player.card_value() > 21):
                    break
                else:
                    continue
        
            elif(action == 2):
                stand()
                break

            else:
                print('Please enter a valid option! \n')

def place_bet():    
    
    while(1):
        print('Your chip balance is : ' +str(mychips.coin_balance()))
        try :
            bet_amount = int(input("\nPlease place your bet. \n"))
        except ValueError:
            print('Enter a value between 1 to your maximum chips! \n')
            
        else:
            if(bet_amount > mychips.coin_balance()):
                print('\nInsufficeint chips! \n')
            else:
                break
    
def hit():
    player.add_card(mydeck.deal()) 

def stand():
    
    player.reset_card_value()
    player.calculate_card_value(player.cards)
    player.ace_correction()

    while(1):
        if(dealer.card_value() < 17):
            dealer.reset_card_value()
            dealer.add_card(mydeck.deal())
            dealer.calculate_card_value(dealer.cards)
            dealer.ace_correction()
        
        elif(dealer.card_value() < 17):
            dealer.reset_card_value()
            dealer.add_card(mydeck.deal())
            dealer.calculate_card_value(dealer.cards)
            dealer.ace_correction()
        
        else:
            break

def winner():

    print('\n')

    if(dealer.card_value() > 21):

        mychips.win_bet(bet_amount)
        player.display_player_cards()
        print('Value of player\'s cards : ' + str(player.card_value()))
        dealer.display_dealer_cards_win()
        print('Value of dealer\'s cards : ' + str(dealer.card_value()))
        print("\nPlayer wins!")

    elif(player.card_value() > 21):

        mychips.lose_bet(bet_amount)
        player.display_player_cards()
        print('Value of player\'s cards : ' + str(player.card_value()))
        dealer.display_dealer_cards_win()
        print('Value of dealer\'s cards : ' + str(dealer.card_value()))
        print("\nPlayer loses!")

    elif(player.card_value() < dealer.card_value()):

        mychips.lose_bet(bet_amount)
        player.display_player_cards()
        print('Value of player\'s cards : ' + str(player.card_value()))
        dealer.display_dealer_cards_win()
        print('Value of dealer\'s cards : ' + str(dealer.card_value()))
        print("\nPlayer loses!")

    elif(player.card_value() > dealer.card_value()):

        mychips.win_bet(bet_amount)
        player.display_player_cards()
        print('Value of player\'s cards : ' + str(player.card_value()))
        dealer.display_dealer_cards_win()
        print('Value of dealer\'s cards : ' + str(dealer.card_value()))
        print("\nPlayer wins!")

    elif(player.card_value() <= 21 and dealer.card_value() <= 21 and player.card_value() == dealer.card_value()):

        player.display_player_cards()
        print('Value of player\'s cards : ' + str(player.card_value()))
        dealer.display_dealer_cards_win()
        print('Value of dealer\'s cards : ' + str(dealer.card_value()))
        print('\nDealer pushes.')
    
   
    

if __name__ == '__main__':
    
    mychips = Chips()

    while(1):
        mydeck = Deck()
        mydeck.shuffle()

        player = Hand()
        dealer = Hand()
    
        player.add_card(mydeck.deal())
        player.add_card(mydeck.deal())
    
        dealer.add_card(mydeck.deal())
        dealer.add_card(mydeck.deal())
        dealer.calculate_card_value(dealer.cards)
        dealer.ace_correction()

        player.display_player_cards()
        dealer.display_dealer_cards()

        place_bet()

        action()

        winner()

        while(1):
            ans = input('\nDo you want to try again? Enter Yes or No. \n').title()

            if(ans == 'Yes'):
                break
            elif(ans == 'No'):
                break
            else:
                print('Please enter a valid option.')

        if(ans == 'Yes'):
            continue
        else:
            break


    
