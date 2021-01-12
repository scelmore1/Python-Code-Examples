# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0902

Scott Elmore
11/15/19

 “I have not given or received any
unauthorized assistance on this assignment”



YouTube Link : https://youtu.be/9Uc8cccnmAg
"""

# import packages
import numpy as np
from matplotlib import pyplot as plt
import time


def displayBoard(b):
    'display the passed in board, numpy NxN array'
    plt.imshow(b, interpolation='nearest')
    # looks better without axes
    plt.axis('off')
    plt.show()


def advance(b, t=0):
    '''accept a board b, advance it t steps, while creating a new board following
    Conway's Game of Life rules'''
    # continue to advance until iterate through all steps
    if t > 0:
        # make a copy so original board isn't being modified
        new_board = b.copy()

        # get the board dimensions
        dim = len(b)
        for i in range(dim):
            for j in range(dim):
                # create counting variable to track status of neighbors
                neighbors = 0

                # sum neighbors, board acts as torus
                neighbors += b[i, (j + 1) % dim]
                neighbors += b[i, (j - 1) % dim]
                neighbors += b[(i + 1) % dim, j]
                neighbors += b[(i - 1) % dim, j]

                # get status of current cell
                if b[i, j]:
                    # get new number based on rules
                    if neighbors < 2:
                        new_num = 0
                    elif neighbors < 4:
                        new_num = 1
                    else:
                        new_num = 0
                else:
                    new_num = int(neighbors == 3)

                # set new board to new number
                new_board[i, j] = new_num

        # display board as well as current iteration
        print('\nBoard Iteration {}'.format(advance_steps - t + 1))
        displayBoard(new_board)

        # sleep to help visaulize board advancement
        time.sleep(.3)

        # call advance after subtracting a step
        advance(new_board, t - 1)


def populateBoard(arr, prob):
    'populate a Game of Life board (0 or 1) given a random numpy NxN array'

    # iterate over arrau
    with np.nditer(arr, op_flags=['readwrite']) as it:
        for x in it:
            # overwrite array by setting x to 1 where random value is less than
            # passed in probability
            x[...] = (x < prob)
    return arr


def conway(s, p):
    'given a size s and probability p, create a Conway Game of Life board'

    # use numpy random to create a random 0-.99 board
    board = populateBoard(np.random.random((s, s)), p)
    print('\nRandomly Populated Board')
    displayBoard(board)
    t = advance_steps
    advance(board, t)


def Main():
    'run examples'

    global advance_steps
    advance_steps = 10
    conway(100, .1)
    conway(100, .5)
    conway(100, .3)
    conway(50, .3)


Main()
