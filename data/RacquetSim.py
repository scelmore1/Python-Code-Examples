# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:00:39 2019

@author: Scott
"""
import random

def gameOver(a,b):    
    # a and b are scores for players in a racquetball game    
    # RETURNS true if game is over, false otherwise 
    return a == 15 or b == 15

def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players A and B
    # RETURNS A's final score, B's final score
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random.random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random.random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players A and B
    # RETURNS number of wins for A, number of wins for B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:winsB = winsB + 1
    return winsA, winsB

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.    
    n = winsA + winsB
    print("\nGames simulated:", n)
    print( "Wins for A: " + str(winsA)        
        + " (" + str(winsA/n*100) + ")" )
    print( "Wins for B: " + str(winsB)
        + " (" + str(winsB/n*100) + ")" )
    
def getInputs():
    # RETURNS probA, probB, number of games to simulate
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n
    
def main():   
#    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)