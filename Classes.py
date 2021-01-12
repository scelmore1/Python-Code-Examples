# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0501

Scott Elmore
10/25/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/8JJyhblQ9V8
"""

#for using randint
import random

class SixSidedDie:
    'represents a six sided die that can be rolled and shown its given value'
    
    def __init__(self):
        'initalize die with 6 sides and set the current face value to a random ' \
        'int between 1 and 6'
        self.no_sides = 6
        self.face_val = random.randint(1, self.no_sides)
    
    def __repr__(self):
        'when called, return a string like SixSidedDie(3)'
        return self.__class__.__name__ + '(' + str(self.face_val) + ')'

    def roll(self):
        'roll dice; randomize new face value between 1 and 6'
        self.face_val = random.randint(1, self.no_sides)
        return self.getFaceValue()
        
    def getFaceValue(self):
        'return the current face value'
        return self.face_val


class TenSidedDie(SixSidedDie):
    'represents a ten sided die that can be rolled and shown its given value ' \
    'extends SixSidedDie'

    def __init__(self):
        'initalize die with 6 sides and set the current face value to a random ' \
        'int between 1 and 10'
        self.no_sides = 10
        self.face_val = random.randint(1, self.no_sides)


class TwentySidedDie(SixSidedDie):
    'represents a twenty sided die that can be rolled and shown its given value ' \
    'extends SixSidedDie'

    def __init__(self):
        'initalize die with 6 sides and set the current face value to a random ' \
        'int between 1 and 20'
        self.no_sides = 20
        self.face_val = random.randint(1, self.no_sides)


class Cup:
    'represents a cup that holds any number of six, ten, and twenty sided die. '\
    'Can be rolled and shown its sum'
    
    def __init__(self, no_six=1, no_ten=1, no_twenty=1):
        'use default parameters to set number of dice to 1 for each, '\
        'else pass in the number of dice to use'
        #create empty list of dice
        self.dice = []
        #for each number of dice passed in, create a dice of that Class,
        #and add to dice list
        for i in range(no_six):
            self.dice.append(SixSidedDie())
        for i in range(no_ten):
            self.dice.append(TenSidedDie())
        for i in range(no_twenty):
            self.dice.append(TwentySidedDie())

    def __repr__(self):
        'when called, return a string like '\
        'Cup(SixSidedDie(6), TenSidedDie(4), TwentySidedDie(16)'
        return self.__class__.__name__ + '(' + str(self.dice)[1:-1] + ')'

    def roll(self):
        'roll each die within the list of dice'
        for die in self.dice:
            die.roll()
        return self.getSum()

    def getSum(self):
        'sum each of the face values of each of the dice in the list'
        #keep sum variable to add face values while iterating list
        sum_ = 0
        for die in self.dice:
            sum_ += die.getFaceValue()
        return sum_

def Main():
    d = SixSidedDie()
    print(d.roll()) 
    print(d.getFaceValue())
    print(d)
    
    cup = Cup(1,1,1)
    cup = Cup(3,0,0)
    cup = Cup()
    cup = Cup(1,2,1)
    print(cup.roll())
    print(cup.getSum())
    print(cup)
    
if __name__ == "__main__": 
    Main()