# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0101

Scott Elmore
9/20/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/SBqHp_ayePg
"""


def HomeworkGrade():
    # docstring for the HomeworkGrade function
    '''returns the appropriate grade for
    a student based on input parameters'''

    # initialize grade variable to a 0 float, can return grade of 0 when exiting if condition block
    grade = 0.0

    # make sure user submits either Y or N as to simplify logic
    print('\nPlease answer the following questions as either Y or N')

    # first Y/N string
    submit = input('Did the student submit a single uncompressed .py file?')
    # enter into first if conditional block
    if submit.upper() == 'Y':

        # second Y/N string
        name = input('Did the student include their name and date?')
        # enter into second if conditional block
        if name.upper() == 'Y':

            # third Y/N string
            honor = input('Did the student include the honor statement?')
            # enter into third if conditional block
            if honor.upper() == 'Y':

                # fourth Y/N string
                youtube = input(
                    'Did the student include a link to an unlisted YouTube video?')
                # enter into fourth if conditional block
                if youtube.upper() == 'Y':

                    # make sure user submits following questions as a number 0 - 10
                    print(
                        '\nPlease answer the following questions as a number 0 through 10')
                    # use eval() to return an interger value to the variables points
                    points = eval(
                        input('Out of ten points, how would you evaluate the correctness of the code?'))
                    # add next question to points variable
                    points += eval(
                        input('Out of ten points, how would you evaluate the elegance of the code?'))
                    # add next question to points variable
                    points += eval(
                        input('Out of ten points, how would you evaluate the code hygiene?'))
                    # add next question to points variable
                    points += eval(input(
                        'Out of ten points, how would you evaluate the quality of the discussion in the video?'))

                    print('\nPlease answer the following question as a number')
                    # this variable keeps track of how many hours late the assignment was
                    late = eval(
                        input('How many hours late was the assignment?'))
                    # make late worth 1% of the total points available, or .4 of a point
                    late = late * .4

                    # subtract the late points from the points variable
                    points = points - late
                    if points > 0:
                        # make the output grade the number of points calculated, don't return a negative number
                        grade = points
    return grade


print(HomeworkGrade())
