# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0401

Scott Elmore
10/15/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://www.youtube.com/watch?v=-X_ucqpjzkY
"""
import random


def binSearch(sorted_nums, n, index):
    '''binary seach algoritm in O(log n) complexity.
    Seraches the list sorted_nums for the number n and
    makes sure it's not the same number from the index
    passed in. Return True if found, False otherwise.'''
    # set first and last parameters, last is length of list
    first = 0
    last = len(sorted_nums) - 1

    # found parameter for loop exit condition
    found = False

    # continue to loop until found or end of search
    while(first <= last and not found):
        # set mid to floor of midpoint
        mid = (first + last)//2

        # if number found and not the same as the given index, return True
        if sorted_nums[mid] == n and mid != index:
            found = True
        else:
            # continue to iterate with new first and last parameters
            if n < sorted_nums[mid]:
                last = mid - 1
            else:
                first = mid + 1
    # return whether or not number is found
    return found


def iterList(sorted_nums, n):
    '''iterate through the list of sorted nums; O(n) complexity.
    For each number run binSearch() to check for the corresponding 
    number that will sum to n (n - num). Make sure binSearch is not 
    returning own number by iterating with index.'''
    # iterate numbers in sorted_nums, get index with enumerate
    for i, num in enumerate(sorted_nums):
        # if correct number if found; stop iterating
        if binSearch(sorted_nums, n - num, i):
            # return the first number of the sum for print purposes
            return num
    # return None for print purposes
    return None


def toSortedList(i):
    '''create a sorted list of length i of random numbers 0 through 100.'''
    # initialize empty randoms list
    randoms = []
    for x in range(i):
        # add a random integer 0-100 to list
        randoms.append(random.randint(0, 100))

    # use python list sort for sorted list; O(n log n) complexity
    randoms.sort()
    return randoms


def getFromUser():
    '''prompt and return both the size of the random list of integers, i, and the number
    n of which to check if two numbers in the list sum to that number n.'''

    i = eval(input(
        'How many numbers between 0 to 100 would you like to check? Must be greater than 1: '))
    n = eval(input('What number would you like to sum to? '))
    return i, n


def Main():
    '''Main program for Goldbach Deuce. Get parameters from user, make a random list of integers
    and then use Binary Search to check if there are two integers which add to a number n.'''

    i, n = getFromUser()
    # random, sorted list of integers 0-100
    sorted_nums = toSortedList(i)

    # first_num is first number in addition, therefore n-first_num is second
    first_num = iterList(sorted_nums, n)
    if first_num is not None:
        print('\nThe randomly generted list has two numbers that sum to ' + str(n)
              + ':\n\t' + str(first_num) + ' + ' + str(n-first_num) + ' = ' + str(n))
    else:
        # number was not found
        print(
            '\nThe randomly generated list does not contain numbers that sum to ' + str(n))


Main()
