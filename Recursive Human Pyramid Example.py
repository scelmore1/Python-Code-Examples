# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:10:58 2019

@author: Scott
"""

# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0402

Scott Elmore
10/15/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://www.youtube.com/watch?v=od_etNb8OsQ
"""


def humanPyramid(row, column):
    '''create a recursive function where given row and column it returns the
    weight of people atop the given row and column'''
    # base case when row is 0
    if row == 0:
        return 0
    # if column has no upper left, get only upper right, + 64 lbs
    elif column == 0:
        return 64 + .5 * (humanPyramid(row - 1, column))
    # if column has no upper right, get only upper left, + 64 lbs
    elif column == row:
        return 64 + .5 * (humanPyramid(row - 1, column - 1))
    else:
        # else get both upper left and upper right, + 128 lbs
        return 128 + .5 * (humanPyramid(row - 1, column - 1)) + .5 * (humanPyramid(row - 1, column))


def Main():
    '''Main program for running thorugh the iterations of each row and column pair to test
    the corresponding weight on each's back'''

    # tuples corresponding to each pair in the pyramid
    row_col_pairs = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0),
                     (4, 1), (4, 2), (4, 3), (4, 4)]

    # iterate through each pair to print the total weight
    for i, row_col in enumerate(row_col_pairs):
        weight = humanPyramid(row_col[0], row_col[1])
        print('Person ' + chr(ord('A')+i) +
              ' has a weight of ' + str(weight) + ' lbs on them.')


Main()
