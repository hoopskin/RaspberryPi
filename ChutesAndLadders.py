#!/usr/local/bin/python2.7
import random
numOfPlayers = 3
playerPositions = [0]*numOfPlayers
currentPlayer = 1
ladder = [[1,38],[4,14],[9,31],[21,42],[28,84],[36,44],[51,67],[71,91],[80,100]]
chute = [[16,6],[47,26],[49,11],[56,53],[62,19],[64,60],[93,73],[95,75],[98,78]]

def rollDie():
  return random.randint(1,6)

def determineNextPlayer():
  global currentPlayer
  if (currentPlayer < numOfPlayers):
    currentPlayer += 1
  else:
    currentPlayer = 1

def checkWin():
  if (playerPositions[currentPlayer-1] == 100):
    return currentPlayer
  else:
    return -1

def ladderMove():
  for start, end in ladder:
    if (playerPositions[currentPlayer-1] == start):
      playerPositions[currentPlayer-1] = end
      return
  
def chuteMove():
  for start, end in chute:
    if (playerPositions[currentPlayer-1] == start):
      playerPositions[currentPlayer-1] = end
      return
  

def main():
  winner = -1
  turns = 1
  while (winner == -1):
    die = rollDie()
    print playerPositions
    print currentPlayer
    if (playerPositions[currentPlayer-1] + die <= 100):
      playerPositions[currentPlayer-1] += die
      ladderMove()
      chuteMove()
      winner = checkWin()
    determineNextPlayer()
    turns += 1
    
  print "Winner is Player" + str(winner) + " after " + str(turns) + " turns."
  
main()