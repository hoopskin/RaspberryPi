#!/usr/local/bin/python2.7
import random
import itertools
unShuffledDeck = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]
shuffledDeck = []
placedCards = []
p1Hand = []
p2Hand = []
p3Hand = []
p4Hand = []
p1LuckyCount = 0
p2LuckyCount = 0
p3LuckyCount = 0
p4LuckyCount = 0
currentPlayer = 1

def rollDice(numOfDice):
  total = []
  #Roll each dice & add it to the list
  for x in xrange(numOfDice):
    total.append(random.randint(1,6))
  return total

def shuffle():
  for x in xrange(24):
    #Choose a card, remove it from unShuffled & add it to shuffled
    card = random.choice(unShuffledDeck)
    unShuffledDeck.remove(card)
    shuffledDeck.append(card)
  
def dealCards():
  for x in xrange(6):
    #6*4 = 24, done this way instead of if statements with mods for ease
    p1Hand.append(shuffledDeck.pop())
    p2Hand.append(shuffledDeck.pop())
    p3Hand.append(shuffledDeck.pop())
    p4Hand.append(shuffledDeck.pop())  
  p1Hand.sort()
  p2Hand.sort()
  p3Hand.sort()
  p4Hand.sort()

def checkForWinner():
  #If a player has no cards in their hand or they have 7 lucky cards, they win
  if (len(p1Hand) == 0) or (p1LuckyCount == 7):
    return 1
  if (len(p2Hand) == 0) or (p2LuckyCount == 7):
    return 2
  if (len(p3Hand) == 0) or (p3LuckyCount == 7):
    return 3
  if (len(p4Hand) == 0) or (p4LuckyCount == 7):
    return 4
  #Added this because if no one has one, -1 is the value we want for the while loop
  return -1
  
def determineNextPlayer():
  global currentPlayer
  #Turn goes 1 > 2 > 3 > 4 > 1...
  if (currentPlayer == 1):
    currentPlayer = 2
    return
  if (currentPlayer == 2):
    currentPlayer = 3
    return
  if (currentPlayer == 3):
    currentPlayer = 4
    return
  if (currentPlayer == 4):
    currentPlayer = 1
    return
  
def checkAndPlaceLucky(dice):
  global currentPlayer
  #Check hand for cards
  if (hasLuckyCards(dice)):
    #Add to lucky count
    exec "p" + str(currentPlayer) + "LuckyCount += 1"
    #Place cards
    for die in dice:
      placedCards.append(die)
      exec "p" + str(currentPlayer) + "Hand.remove(die)"
    return True
  return False

def hasLuckyCards(dice):
  global currentPlayer
  hasCards = True
  cards = []
  
  #Place cards in local variable
  exec "for card in p" + str(currentPlayer) + "Hand: cards.append(card)"
  
  #Check if the dice are the same number
  if not (dice[0] == dice[1]):
    #For each dice, check the count (which is 0 if it isn't in the list)
    for die in dice:
      if (cards.count(die) == 0):
        hasCards = False
  else:
    #Check if first die is in the cards
    if (cards.count(dice[0]) == 0):
      hasCards = False
    else:
      #Check if die is in subset of cards
      if (cards[cards.index(dice[0])+1:].count(dice[1]) == 0):
        hasCards = False
  return hasCards
  
def pickUpCards():
  exec "p" + str(currentPlayer) + "Hand.extend(placedCards)"
  while (len(placedCards) > 0):
    placedCards.pop()
  #for card in placedCards:
  #UNTESTED: Pop each card into the player's hand
  #exec "p" + str(currentPlayer) + "Hand.append(placedCards.pop())"
    
def placeCards(dice):
  total = 0
  cards = []
  numOfCards = 1
  
  #Get total
  for die in dice:
    total += die
  
  #Place cards in local variable
  exec "for card in p" + str(currentPlayer) + "Hand: cards.append(card)"
  
  #While we can place more cards down
  while(numOfCards <= len(cards)):
    #Get each possible combination
    combinations = itertools.combinations(cards, numOfCards)
    for combination in combinations:
      #Check if the sum of cards == total, if it is, play those cards
      if (sum(combination) == total):
        for card in combination:
          placedCards.append(card)
          exec "p" + str(currentPlayer) + "Hand.remove(card)"
        return True
    numOfCards += 1
  return False
    
  
  
def main():
  #Shuffle and deal
  shuffle()
  dealCards()
  
  winner = -1
  turns = 1
  #While there isn't a winner
  while (winner == -1):
  #while (turns <= 10):
    #DEBUG: Print hands & dice
    print "-----Player " + str(currentPlayer) + "'s Turn-----"
    print "---Hands---"
    print p1Hand
    print p2Hand
    print p3Hand
    print p4Hand
    print "---Hands---"
    print ""
    print "---Placed Cards---"
    print placedCards
    print "---Placed Cards---"
    print ""
    print "---Rolling...---"
    #Roll dice
    dice = rollDice(2)
    print dice
    print "---Rolled---"
    print ""
    
    
    if not (checkAndPlaceLucky(dice)):
      print "Didn't place lucky"
      if not (placeCards(dice)):
        print "Didn't place cards... picking up cards"
        pickUpCards()
    
    determineNextPlayer()
    winner = checkForWinner()
    turns += 1
  
  print "Winner is Player" + str(winner) + " after " + str(turns) + " turns."
    
main()