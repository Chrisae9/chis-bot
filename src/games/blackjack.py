import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

class Blackjack():
    def __init__(self, player):
        self.player = player

    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __str__(self):
            return self.rank + " of " + self.suit


    class Deck:
        def __init__(self):

            self.deck = []
            for suit in suits:
                for rank in ranks:
                    # Create the Card Object
                    self.deck.append(Blackjack.Card(suit, rank))

        def __str__(self):
            deck_comp = ' '
            for card in self.deck:
                deck_comp += "\n" + card.__str__()
            return "The deck has: " + deck_comp

        def shuffle(self):
            random.shuffle(self.deck)

        def deal(self):
            single_card = self.deck.pop()
            return single_card


    class Hand:
        def __init__(self):
            self.cards = []  # start with an empty list as we did in the Deck class
            self.value = 0   # start with zero value
            self.aces = 0    # add an attribute to keep track of aces

        def add_card(self, card):
            # card will be passed in from Deck.deal()
            self.cards.append(card)
            self.value += values[card.rank]

            if card.rank == "Ace":
                self.aces += 1

        def adjust_for_ace(self):

            # This code changes an ace from 11 to 1 when you are over 21
            while self.value > 21 and self.aces > 0:
                self.value -= 10
                self.aces -= 1


    class Chips:

        def __init__(self, total=100):
            self.total = total  # This can be set to a default value or supplied by a user input
            self.bet = 0

        def win_bet(self):
            self.total += self.bet

        def lose_bet(self):
            self.total -= self.bet


    def take_bet(self, chips):

        while True:

            try:
                chips.bet = int(input(
                    f"You currently have {chips.total} chips. How many would you like to bet? "))
            except:
                print("Please provide an integer")
            else:
                if chips.bet > chips.total:
                    print(
                        f"Sorry, you do not have enough chips! You only have {chips.total}.")
                else:
                    break


    def hit(self, deck, hand):

        hand.add_card(deck.deal())
        hand.adjust_for_ace


    def hit_or_stand(self, deck, hand):
        global playing  # to control an upcoming while loop

        while True:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

            if x[0].lower() == 'h':
                self.hit(deck, hand)

            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                playing = False

            else:
                print("Sorry, please try again.")
                continue
            break


    def show_some(self, player, dealer):
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print('', dealer.cards[1])
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("The value of your hand is ", player.value)


    def show_all(self, player, dealer):
        print("\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =", dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =", player.value)


    def player_busts(self, player, dealer, chips):
        print("Player Bust!")
        chips.lose_bet()


    def player_wins(self, player, dealer, chips):
        print("Player Wins!")
        chips.win_bet()


    def dealer_busts(self, player, dealer, chips):
        print("Player Wins! Dealer Busted!")
        chips.win_bet()


    def dealer_wins(self, player, dealer, chips):
        print("Dealer Wins!")
        chips.lose_bet()


    def push(self, player, dealer):
        print("Dealer and player tie! PUSH")


    def start(self):
        global playing
        # Set up the Player's chips
        player_chips = Blackjack.Chips(100)

        while True:
            # Print an opening statement
            print("Welcome to Blackjack")

            # Create & shuffle the deck, deal two cards to each player
            deck = self.Deck()
            deck.shuffle()

            player_hand = self.Hand()
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())

            dealer_hand = self.Hand()
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

            # Prompt the Player for their bet
            self.take_bet(player_chips)

            # Show cards (but keep one dealer card hidden)
            self.show_some(player_hand, dealer_hand)

            while playing:  # recall this variable from our hit_or_stand function

                # Prompt for Player to Hit or Stand
                self.hit_or_stand(deck, player_hand)

                # Show cards (but keep one dealer card hidden)
                self.show_some(player_hand, dealer_hand)

                # If player's hand exceeds 21, run player_busts() and break out of loop
                if player_hand.value > 21:
                    self.player_busts(player_hand, dealer_hand, player_chips)
                    break

            # If Player hasn't busted, play Dealer's hand until Dealer is equal to or less than player
            if player_hand.value <= 21:

                while dealer_hand.value < player_hand.value:
                    self.hit(deck, dealer_hand)

                # Show all cards
                self.show_all(player_hand, dealer_hand)

                # Run different winning scenarios
                if dealer_hand.value > 21:
                    self.dealer_busts(player_hand, dealer_hand, player_chips)
                elif dealer_hand.value > player_hand.value:
                    self.dealer_wins(player_hand, dealer_hand, player_chips)
                elif player_hand.value > dealer_hand.value:
                    self.player_wins(player_hand, dealer_hand, player_chips)
                else:
                    self.push(player_hand, dealer_hand)

            # Inform Player of their chips total
            print(f"\n Player total chips are at: {player_chips.total}")

            # Ask to play again
            new_game = input("Would you like to play another hand? y/n \n")
            if new_game[0].lower() == "y":
                playing = True
                continue
            elif new_game[0].lower() == 'n':
                print("Thank you for playing!")
                break
            else:
                continue