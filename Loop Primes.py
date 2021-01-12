# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0301

Scott Elmore
10/08/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/q1vW4ZW0_Ao
"""


def primes_sieve(upper_bound):
    '''the Sieve of Eratosthenes algorithm is an efficient way 
    for finding prime numbers.  The algo works by crossing out 
    all the composites within the range we give it.  The algo 
    terminates once checking through the squareroot of n, as it
    is unnecceassry to check through this point. For more info:
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes'''

    # initialize an empty array for the prime numbers
    primes = []

    # initalize an array of Boolean variables all set to true
    prime = [True] * upper_bound

    # numbers 0 and 1 are not prime
    prime[0] = prime[1] = False

    # start with finding all multiples of 2
    p = 2
    while (p*p <= upper_bound):
        if (prime[p] == True):
            # all the multiples of the number p are known to be not prime
            for i in range(p*2, upper_bound, p):
                prime[i] = False
        # increase p to the next number to check
        p += 1

    for p in range(upper_bound):
        if prime[p]:
            # append to primes list where prime is True after running algo
            primes.append(p)

    # primes returns all prime numbers through the given upper_bound, in this case 100
    return primes


def primeIter(prime_nums, even):
    '''checks each prime number contained in the primes
    list to see if any combination (including with itself)
    creates the even number, and prints the output'''
    # iterate through the entirety of the primes array
    for i in range(len(prime_nums)):
        # nested loop iterates through the entirety of the primes array
        for j in range(len(prime_nums)):
            # check to see if condition is satisified, print ouput and return
            if even == prime_nums[i] + prime_nums[j]:
                print(str(even) + ' = ' + str(prime_nums[i])
                      + ' + ' + str(prime_nums[j]))
                return


def loopEvens(prime_nums, upper_bound):
    '''loops over the range of even numbers from 4 to 100 
    and calls primeIter to find the two prime numbers that
    total the given even number'''
    # loop all even numbers from 4 to 100
    for even in range(4, upper_bound, 2):
        primeIter(prime_nums, even)


def Main():
    '''Main program for checking Goldbach's Conjecture,
    that all even numbers are the result of two primes 
    being added together.  Test through the number 100.'''
    
    # set bound to 100 since we only need primes under 100
    upper_bound = 100
    prime_nums = primes_sieve(upper_bound)
    loopEvens(prime_nums, upper_bound)


Main()
