# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0102

Scott Elmore
9/24/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/aa_PuC7I6t0
"""


def coprime_test_loop():
    # docstring for the coprime_test_loop function
    '''asks the user for two numbers then prints out
    a message indicating if the numbers are coprime or not.
    function will continue to run until user exits'''

    # while loop for continuing to run
    # coprime test loop until user exits
    run = True
    while(run):

        # get two numbers from the user
        a = eval(input('Please enter the first number: '))

        b = eval(input('Please enter the second number: '))

        # logic to help the print statement when declaring the numbers coprime or not
        not_str = ' not'
        if coprime(a, b):
            not_str = ''

        print('The numbers ' + str(a) + ' and ' +
              str(b) + ' are' + not_str + ' coprime.')

        # determine if user would like to exit
        exit_ = input('Would you like to exit, Y or N?')
        if exit_.upper() == 'Y':
            run = False


def coprime(a, b):
    # docstring for the coprime function
    '''returns true or false depending on if a
    and b are coprime'''

    # helps avoid an unneccessary loop if both numbers are even
    if not(a % 2) and not(b % 2):
        return False

    # logic saves one iteration of the loop by having the larger number
    # mod divide by the smaller one
    if abs(a) < abs(b):
        t = a
        a = b
        b = t

    # logic is derived from the euclidean algorithm for finding the GCD of two numbers
    # see https://en.wikipedia.org/wiki/Euclidean_algorithm for information on what
    # the algorithm does.  Two numbers are coprime if their GCD is 1.
    while(b != 0):
        t = b
        b = a % b
        a = t

    # check to see if GCD is 1 or -1 (if given a negative number)
    return a == 1 or a == -1


coprime_test_loop()
