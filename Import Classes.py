# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0502

Scott Elmore
10/25/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/_WFnW6vjGaM
"""

from DSC430_A0501 import Cup
import random


def greetUser():
    '''function for greeting user and getting name'''
    name = input('Hi there! What\'s your name?')
    play_str = input('\nWould you like to play a little game? I\'ll give you $100 and'
                     ' you get to see if you can increase it by rolling a cup of dice.'
                     '  Press Y to continue')
    play = False
    # only play if user inputs y or Y
    if play_str.upper() == 'Y':
        play = True
    return name, play


def getFromUser(balance):
    '''function for getting bet amount and number of dice of each type from user'''
    bet = eval(input('\nSo how much money you willing to wager?'))
    # prevent user from betting negative or above their balance
    if bet < 0 or bet > balance:
        print('Who do you think you\'re fooling here? Bet between 0 and your balance before I call the FBI.')
        # recursively call this function again until user inputs appropriate amount
        return getFromUser(balance)
    die6 = eval(input('How many 6 Sided Die woule you like to roll?'))
    die10 = eval(input('How many 10 Sided Die woule you like to roll?'))
    die20 = eval(input('How many 20 Sided Die woule you like to roll?'))

    # return bet amount and dice as tuple
    return bet, (die6, die10, die20)


def adjustBal(cup_sum, goal_num, balance, bet):
    '''function for returning the new balance based off the cup sum and the goal number'''
    # lose bet if gone over
    if cup_sum > goal_num:
        return balance - bet
    # win 10x bet if numbers match
    elif cup_sum == goal_num:
        return balance + bet*10
    # win 5x bet if number within 3
    elif cup_sum >= goal_num - 3:
        return balance + bet*5
    # win 2x bet if number within 10
    elif cup_sum >= goal_num - 10:
        return balance + bet*2
    # win nothing, lose nothing if not within 10
    else:
        return balance


def printOutputs(balance, difference, name):
    '''function for printing outputs to user about current balance and result of last roll'''
    # exit when balance comes to 0
    if balance <= 0:
        print('GAME OVER. Balance is equal to zero. YOU LOSE. MWAHAHA')
        quit_ = 'EXIT'
    else:
        # different outputs depend on how last roll went
        if difference > 0:
            quit_ = input('$$$CHA-CHING$$$ ' + name + ' you won ' + str(difference)
                          + '!. Your balance is now ' +
                          str(balance) + '. If you would like to continue '
                          'press enter, else type exit to quit.')
        elif difference < 0:
            quit_ = input('WOMP WOMP WOOOOMP :( ' + name + ' you lost '
                          + str(difference) + '!. Your balance is now ' +
                          str(balance) + '. If you would like '
                          'to continue press enter, else type exit to quit.')
        else:
            quit_ = input('Are you even trying to win? Be more aggressive ' + name +
                          '.  Your balance is still ' +
                          str(balance) + '. If you would like '
                          'to continue press enter, else type exit to quit.')
    return quit_


def Main():
    '''main function for running the game engine code'''
    # first greet user
    name, playing = greetUser()

    # set inital balance to 100
    balance = 100

    # contine to loop until user exits or balance is 0
    while(playing):
        # get the number user needs to match by using random.randint()
        goal_num = random.randint(1, 100)
        print('\nOK.\nHere we go.\nYou need to get as close to ' +
              str(goal_num) + ' as possible, without going over.')

        # get both beth amount and number of dice from user
        bet, dice = getFromUser(balance)

        # initalize a cup with the given dice amounts
        cup = Cup(dice[0], dice[1], dice[2])
        print('\nYou rolled... \n' + str(cup.roll()) + '!!!!!!')

        # adjust the balance based off what the cup rolled and how much they bet
        new_bal = adjustBal(cup.getSum(), goal_num, balance, bet)
        difference = new_bal - balance
        balance = new_bal

        # call function to print the ouputs based on the current balance, return quit if exiting loop
        quit_ = printOutputs(balance, difference, name)

        if quit_.upper() == 'EXIT':
            playing = False


Main()
