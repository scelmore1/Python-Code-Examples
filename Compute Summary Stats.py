# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0601

Scott Elmore
10/29/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/CZOkpNIezL0
"""

import os
import csv
import statistics as stat
import math

# set a constant variable for number of buckets to use in median algorithm
NUM_BUCKETS = 11


def getFromFile(var_name):
    '''helper function for returning list of the specified var_name from a column of 
    a csv table'''
    # library to return current path
    dirpath = os.getcwd()

    # open avocad.csv file in current path
    # with keyword to properly close on exit
    with open(os.path.join(dirpath, 'avocado.csv')) as infile:
        # csv library for reading only specified column in csv
        reader = csv.DictReader(infile)
        var_list = []
        for row in reader:
            for variable, val in row.items():
                # if variable is equal to the given var_name
                if var_name == variable:
                    # convert value to float, add to list
                    var_list.append(float(val))
    return var_list


def readAndComputeMean_SM(var_name):
    '''function computes mean using stats module'''
    var_list = getFromFile(var_name)
    return stat.mean(var_list)


def readAndComputeSD_SM(var_name):
    '''function computes standard deviation using stats module'''
    var_list = getFromFile(var_name)
    return stat.stdev(var_list)


def readAndComputeMedian_SM(var_name):
    '''function computes median using stats module'''
    var_list = getFromFile(var_name)
    return stat.median(var_list)


def readAndComputeMean_HG(var_name):
    '''function computes mean using homegrown approach'''
    var_list = getFromFile(var_name)

    # mean is equal to (sum of vars list) / (count of vars in list)
    return sum(var_list) / len(var_list)


def readAndComputeSD_HG(var_name):
    '''function computes standard deviation using homegrown approach'''
    var_list = getFromFile(var_name)

    # first get mean using previous function, to be used in algorithm
    mean = readAndComputeMean_HG(var_name)

    # calculate sum of squares using mean for each number in list
    ss = sum((x - mean)**2 for x in var_list)

    # std dev is equal to sqrt of sum of squares divided by length of list - 1
    return math.sqrt(ss / (len(var_list) - 1))


def readAndComputeMedian_HG(var_name):
    '''function computes median using homegrown approach'''
    var_list = getFromFile(var_name)

    # first sort the list
    var_list.sort()

    # median is found at the middle of the list if odd, if even extra step required
    mid = len(var_list) // 2

    # if list is odd this line adds the same number and divides by 2, if even
    # this line will add the two middle points in the list and divide by 2
    return (var_list[mid] + var_list[~mid]) / 2


def readAndComputeMean_MML(var_name):
    '''function computes mean using memory-less approach'''
    dirpath = os.getcwd()

    # keep track of variables sum and count
    var_sum = 0
    var_count = 0

    # open file to read each line one at a time
    with open(os.path.join(dirpath, 'avocado.csv')) as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            for variable, val in row.items():
                if var_name == variable:
                    # add variable to sum
                    var_sum += float(val)

                    # increment count by 1
                    var_count += 1

    # mean is equal to sum / count
    return var_sum / var_count


def readAndComputeSD_MML(var_name):
    '''function computes standard deviation using memory-less approach'''
    dirpath = os.getcwd()
    # keep track of sum of squares and count
    var_sum_sqaures = 0
    var_count = 0

    # first get mean using memory-less approach
    mean = readAndComputeMean_MML(var_name)

    # open file to read one line at a time
    with open(os.path.join(dirpath, 'avocado.csv')) as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            for variable, val in row.items():
                if var_name == variable:
                    # add to sum of squares using (val - mean)^2
                    var_sum_sqaures += (float(val) - mean)**2

                    # increment count by 1
                    var_count += 1

    # std dev is equal to sqrt of sum of squares divided by total count - 1
    return math.sqrt(var_sum_sqaures / (var_count - 1))


def medianInsert(val, var_counter_list, bucket_width, min_val):
    '''function for figuring out which bucket in the var_counter_list needs to be incremented'''

    # only increment count in buckets 1 through NUM_BUCKETS
    for i in range(1, NUM_BUCKETS):
        if val < (min_val + i*bucket_width):
            # increment count by 1 if value < min_val + i * bucket_width
            var_counter_list[i] += 1
            return


def medianSearch(total_cnt, var_counter_list, bucket_width, min_val):
    '''function for determining if median has been found and what the new min and max will be'''

    # initialize new min and max to 0
    new_min = 0
    new_max = 0

    # initialize median_found flag to False
    median_found = False

    # current accumulated count is the count contained in var_counter_list[0]
    accum_cnt = var_counter_list[0]

    # iterate through all buckets starting at 1
    for i in range(1, NUM_BUCKETS):
        # increment accumulated count by bucket amount
        accum_cnt += var_counter_list[i]

        # if accumulated count / (total count - 1) equals or exceeds 1/2,
        # exit from loop and check if median is found
        if accum_cnt / (total_cnt - 1) >= .5:
            # median must be contained in the bucket which forced accumulated count
            # to exceed 1/2 total count
            if var_counter_list[i] == 1:
                median_found = True

            # set new min and max
            new_min = min_val + bucket_width*(i - 1)
            new_max = min_val + bucket_width*i

            # var_counter_list[0] is now the accumulated count minus the last bucket added
            var_counter_list[0] += (accum_cnt -
                                    var_counter_list[i] - var_counter_list[0])
            return new_min, new_max, median_found


def readAndComputeMedian_MML(var_name):
    '''function computes median using memory-less approach'''
    dirpath = os.getcwd()

    # flag to be set to True when median found
    median_found = False

    # min_val, max_val, temp_vals set to infinite numbers in order to pass conditionals in
    # first loop through data
    min_val = float('-inf')
    max_val = float('inf')
    potential_max = float('-inf')
    potential_min = float('inf')

    # median sum is used when number of variables is even
    median_sum = 0

    # keep a total count of variables
    total_cnt = 0

    # keep a list of counters, this list is the size of NUM_BUCKETS
    var_counter_list = [0] * NUM_BUCKETS

    with open(os.path.join(dirpath, 'avocado.csv')) as infile:
        while(True):
            # need to go back to beginning of file on each loop
            infile.seek(0)

            # set counters back to 0 on each loop, except var_counter_list[0];
            # which contains discarded items
            for i in range(1, NUM_BUCKETS):
                var_counter_list[i] = 0

            reader = csv.DictReader(infile)
            for i, row in enumerate(reader):
                for variable, val in row.items():
                    if var_name == variable:
                        val = float(val)

                        # if min_val is not infinite, means we're on first loop
                        if min_val != float('-inf'):
                            # if value is within the range of what our buckets are checking
                            if val > min_val and val < max_val:
                                # if median has been found
                                if median_found:
                                    # if odd number
                                    if total_cnt % 2 != 0:
                                        # if we aren't calculating from an even number
                                        if median_sum == 0:
                                            # return value
                                            return val
                                        else:
                                            # return (median sum + current value) / 2
                                            return (median_sum + val) / 2
                                    else:
                                        # set median sum to current value
                                        median_sum = val

                                        # increment total_cnt so on next loop it is odd
                                        total_cnt += 1
                                        continue

                                # if median not found, run medianInsert()
                                medianInsert(val, var_counter_list, (max_val - min_val) / (NUM_BUCKETS - 1),
                                             min_val)
                        # this is first loop
                        else:
                            # increment total count
                            total_cnt += 1

                            # find min and max in data
                            if val > potential_max:
                                potential_max = val
                            elif val < potential_min:
                                potential_min = val

            # if not on first loop
            if min_val != float('-inf'):
                # get new min and max, and if median is found by running medianSearch()
                potential_min, potential_max, median_found = medianSearch(total_cnt, var_counter_list,
                                                                          (max_val - min_val) / (NUM_BUCKETS - 1), min_val)
            # set min, max val
            min_val = potential_min
            max_val = potential_max


def statsTable(var):
    '''function for printing stats of a variable from a file according to their methods'''

    print('\nTable of different methods for calculating mean, standard deviation and median from a file '
          'containing data on Avacodo sales.\n\n')
    print('\t\tMean\t\tSt. Dev.\tMedian')
    print('\t\t' + '-'*42)
    print('Stats Module: | {a:.2f}\t{b:.2f}\t{c:.2f} |'.format(a=readAndComputeMean_SM(
        var), b=readAndComputeSD_SM(var), c=readAndComputeMedian_SM(var)))
    print('Homegrown:    | {a:.2f}\t{b:.2f}\t{c:.2f} |'.format(a=readAndComputeMean_HG(
        var), b=readAndComputeSD_HG(var), c=readAndComputeMedian_HG(var)))
    print('Memory-less:  | {a:.2f}\t{b:.2f}\t{c:.2f} |'.format(a=readAndComputeMean_MML(
        var), b=readAndComputeSD_MML(var), c=readAndComputeMedian_MML(var)))
    print('\t\t' + '-'*42)


def Main():
    # calculate stats of variable Total Volume
    var_name = "Total Volume"
    statsTable(var_name)


Main()
