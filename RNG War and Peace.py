# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0701

Scott Elmore
11/01/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/CZJHvcjATpg
"""

import os
import re


class WarAndPeacePseudoRandomNumberGenerator:
    '''a pseudo random number generator class that outputs a random
    number 0 to 1 when random() is called; utilizes text of War and Peace
    to produce random number'''
    
    #text from first chapter starts around character 6500, start here
    seed_init = 6500
    #add more to seed for every time eof is reached
    eof_adder = 1
    
    def __init__(self, seed_def = 0, char_skip = 1000, float_len = 16):
        '''initialize with a seed, an amount of characters to skip ahead in the text
        and the length of the float variable to return'''
        #set default seed to 0, add to the seed initializer
        self.seed_init += seed_def
        
        #set current position to new initalizer amount
        self.current_pos = self.seed_init
        self.float_len = float_len
        self.char_skip = char_skip
        
    
    def getFromFile(self):
        '''open war and peace text file and read two characters a far enough 
        distance apart in order to generate a list of binary variables'''
        #create list of binary numbers
        binary_nums = []
        
        #open war and peace text file in cwd
        with open(os.path.join(os.getcwd(), 'war-and-peace.txt')) as infile:
            #read all characters through the current position amount
            infile.read(self.current_pos)
            
            #continue to loop until length of binary number list is same as length of float variable
            while len(binary_nums) < self.float_len:
                #set two variables x,y to None
                x = None
                y = None
                
                #intialize next_char variable to character next char in file
                next_char = infile.read(1)
                #increment current position whenever a character is read
                self.current_pos += 1
                
                #continue to read character until an a-z letter or reach eof
                while x is None and next_char != '':
                    #match with regex, None if no match
                    x = re.search("[a-zA-Z]", next_char)
                    next_char = infile.read(1)
                    self.current_pos += 1
                    
                #skip ahead a number of characters, to prevent correlated characters
                infile.read(self.char_skip)
                self.current_pos += self.char_skip
                
                #continue to read character until an a-z letter or reach eof
                while y is None and next_char != '':
                    #match with regex, None if no match
                    y = re.search("[a-zA-Z]", next_char)
                    next_char = infile.read(1)
                    self.current_pos += 1
                
                #eof has been reached
                if x == None or y == None:
                    #current position is set to seed initializer plus eof addition
                    self.current_pos = self.seed_init + self.eof_adder
                    #go to point in file that current position is set to
                    infile.seek(self.current_pos)
                    #increment eof_adder for next time
                    self.eof_adder += 100
                else:
                    #compare x and y characters, set to 1 if greater
                    if x.string >= y.string:
                        binary_var = 1
                    else:
                        binary_var = 0
                    binary_nums.append(binary_var)   
                    
        return binary_nums
    
    def calculateFloat(self, binary_nums):
        '''calculate a 16 digit float between 0-1 based on the list of binary numbers'''
        random_float = 0.0
        for i,num in enumerate(binary_nums):
            if num == 1:
                #increment our float by 1 over 2^(i+1)
                #highest number is 1, lowest is 0
                random_float += 1 / 2**(i + 1)
        return random_float
                
            
    def random(self):
        '''gets the next random number'''
        binary_nums = self.getFromFile()
        return self.calculateFloat(binary_nums)
            
    
def getStats(num_list):
    '''print the min, max, and mean of the passed in list'''
    min_rand = min(num_list)
    max_rand = max(num_list)
    mean_rand = sum(num_list) / len(num_list)
    print('\nMin: {}\t\tMax: {}\t\tMean:{}'.format(min_rand, max_rand, mean_rand))
    
def Main():
    '''create two pseudo-random number generators with different seeds, and print statistics'''
    #create list of random numbers
    random_nums = []
    prng = WarAndPeacePseudoRandomNumberGenerator()
    #get 10000 random floats 0-1
    for x in range(10000):
        r = prng.random()
        random_nums.append(r)
    getStats(random_nums)
    
    prng = WarAndPeacePseudoRandomNumberGenerator(12345)
    random_nums = []
    #get 10000 random floats 0-1
    for x in range(10000):
        r = prng.random()
        random_nums.append(r)
    getStats(random_nums)

if __name__ == "__main__":     
    Main() 
    