#Shuffle a deck of card with OOPS in Python
from random import shuffle

class Cards:
    suites = ['Heart', 'Diamond', 'Club', 'Spade']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']
    def __init__(self):
        pass

class Deck(Cards):
    def __init__(self):
        Cards.__init__(self)
        self.mycardset = []
        for n in Cards.suites:
            for c in Cards.values:
                self.mycardset.append(c + ' of ' + n )

class ShuffleCards(Deck):
    def __init__(self):
        Deck.__init__(self)

    def shuffle(self):
        if len(self.mycardset) < 52 :
            print('Cannot Shuffle Cards since some cards are not in deck')
        else:
            shuffle(self.mycardset)
            return self.mycardset

    def popcard(self):
        if len(self.mycardset) == 0 :
            print("Cannot pop card since no more cards")
        else:
            cardpoped = self.mycardset.pop()
            return (cardpoped)

objCards = Cards()
objDeck = Deck()

player1cards = objDeck.mycardset
print('Player 1 cards : \n ',  player1cards)

objShuffleCard = ShuffleCards()

player2cards = objShuffleCard.shuffle()
print('Player 2 cards : \n', player2cards)


