# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0202

Scott Elmore
10/01/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://www.youtube.com/watch?v=ip8ayGPbUX0
"""
import os

def greetUser():
    '''a friendly message to let the user know what the proram does'''

    greet_msg = \
        '\nHello User! Follow the prompts to create a stem and leaf'\
        ' plot given the 3 data files in our current directory. You'\
        ' may continue to make stem and leaf plots or exit when asked.'

    print(greet_msg)


def getUserInput():
    '''prompt user to return 1, 2 or 3'''

    file_index = eval(
        input('Which data file would you like to use, 1, 2, or 3?'))

    # keep asking user for 1, 2, or 3 if they didn't input the right number
    while file_index not in range(1, 4):
        file_index = eval(input('You must\'ve misheard me..., 1, 2, or 3?'))

    # helpful to return number as str
    return str(file_index)


def readFile(file_index):
    '''read the appropriate file given the index and return the
    numbers as a list of strings'''

    # initialize empty list
    num_list = []

    # use with open to ensure file is closed after reading
    # concatanate index with correct path for data
    with open(os.path.join(os.getcwd(), 'StemAndLeaf' + file_index + '.txt'), 'r') as f:
        for line in f:
            # strip the line to remove trailing \n
            num_list.append(line.strip())

    return num_list


def getStemAndLeaf(num_list):
    '''calls more helpful functions dealing with 
    steam and leaf plot format'''

    # important to first sort the list, pass in key=int to sort numerically
    num_list.sort(key=int)

    # call findBreakPoint to get both size of leaf(bp) and the numbers
    # to be used in the stems, pass in num_list
    bp, stem_set = findBreakPoint(num_list)

    # call splitList to get a dictionary with stems as keys, leafs as values
    # pass in num_list, set of stems, and breakpoint
    leaf_dict = splitList(num_list, stem_set, bp)

    # call display to do the actual printing to screen of plot
    display(leaf_dict)


def findBreakPoint(num_list):
    '''return the breakpoint as an integer, 
    return set of unique stems to be used'''
    # only need to check for leaf sizes through the largest value in our num_list
    largest_val = num_list[-1]

    # iterate i, which will be the bp, until the number of
    # unique stems fits within the 'sweetspot'
    for i in range(1, len(largest_val)):

        # initialize empty stems list
        stems = []
        for num in num_list:
            # find stem by taking all digits except for the size of i
            stem = num[:-i]

            # if number of digits can't be found with -i, the stem must be 0
            if stem == '':
                stem = '0'

            # add this stem to stems list
            stems.append(stem)

        # create set out of list of stems to only retain unique values
        stem_set = set(stems)

        # call fillIn function for filling in the stems that exist 'hidden'
        # between the values we have in the num_list
        stem_set = fillIn(list(stem_set))

        # define the sweet spot as number of stems being between 2 and 19
        if len(stem_set) > 1 and len(stem_set) < 20:
            break  # exit for loop
    
    # if no set of stems found that match criteria the whole plot will be leaves
    return i, stem_set


def splitList(num_list, stem_set, bp):
    '''return dictionary for keeping track of which leaves belong to which stem'''

    # create dictionary initialized with the stems from stem_set
    leaf_dict = {key: [] for key in stem_set}
    for num in num_list:
        # the key equaling the digits before the bp will contain a list of
        # all the values equaling the digits beyond the bp
        leaf_dict[num[:-bp]].append(num[-bp])

    return leaf_dict


def display(leaf_dict):
    '''use print stmts to output a well formatted stem and leaf plot'''

    # title
    print('\n\t\tStem and Leaf Plot')

    # iterate through all the stems
    for stem in leaf_dict.keys():
        print('\n')

        # left hand side of plot
        print(stem + ' | ', end='')
        if stem in leaf_dict:
            # get all the leaves in the dicitonary for each stem key
            for leaf in leaf_dict[stem]:
                # print the leaves with a space in between
                print(leaf + ' ', end='')


def fillIn(stems):
    '''use to fill in the set of stems with all the numbers between the min and max'''

    # sort the list of stems in order to use min and max
    stems.sort(key=int)

    # initalize empty list of stems
    new_stems = []

    # iterate through the max stem
    for i in range(int(stems[0]), int(stems[-1])+1):
        # helpful to return stems as str
        new_stems.append(str(i))

    return new_stems


def promptExit():
    '''ask user if they would like to exit, return false to exit main()'s while loop'''

    exit_ = input('\nWould you like to continue to view beautiful stem'
                  ' and leaf plots? Y or N?')

    # return false if user wants to exit
    if exit_.upper() == "N" or exit_.upper() == "NO":
        return False

    return True

def main():
    '''main function'''

    # set initial condition to true for while loop
    loop = True
    while(loop):
            
        # function first greets user
        greetUser()

        # function gets index number
        file_index = getUserInput()

        # function reads the appropriate file
        num_list = readFile(file_index)

        # function then displays stem and leaf
        getStemAndLeaf(num_list)

        # continue to loop until user exits
        loop = promptExit()
                
if __name__ == "__main__":
    main()
