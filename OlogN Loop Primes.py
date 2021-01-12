# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0302

Scott Elmore
10/08/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/drV480llJIY
"""

def primes_sieve(upper_bound):
    '''the Sieve of Eratosthenes algorithm is an efficient way 
    for finding prime numbers.  The algo works by crossing out 
    all the composites within the range we give it.  The algo 
    terminates once checking through the squareroot of n, as it
    is unnecceassry to check through this point. For more info:
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes'''
    
    #initialize an empty array for the prime numbers
    primes = []
    
    #initalize an array of Boolean variables all set to true
    prime = [True] * upper_bound
    
    #numbers 0 and 1 are not prime
    prime[0] = prime[1] = False
    
    #start with finding all multiples of 2
    p = 2
    while (p*p <= upper_bound):
        if (prime[p] == True):
            #all the multiples of the number p are known to be not prime
            for i in range (p*2, upper_bound, p):
                prime[i] = False
        #increase p to the next number to check
        p += 1
        
    for p in range(upper_bound):
        if prime[p]:
            #append to primes list where prime is True after running algo
            primes.append(p)
            
    #primes returns all prime numbers through the given upper_bound
    return primes

def numberDefinition(number_to_check):
    '''function checks the number given to see if it is contained
    an either of our happy or sad number lists.  If so it prints
    the approriate string and returns False.  If the number is not
    in either of our lists, return True.'''
    
    #set initial variable to False
    happy = False
   
    #condition to see if number is in either list, setting appropriate variable
    if number_to_check in happy_nums:
        happy = True
    elif number_to_check in sad_nums:
        pass
    else:
        #have to now run the happyLoop() on this number 
        return True
    
    #condition to check if number is prime
    prime = False
    if number_to_check in prime_nums:
        prime = True
    
    #set string values to appropriate values for our output
    happy_str = 'happy ' if happy else 'sad '
    prime_str = 'prime' if prime else 'non-prime'
    print('The number ' + str(number_to_check) + ' is a ' \
          + happy_str + prime_str)
    
    #no need to run happyLoop() on this number
    return False
    
def happyLoop(number_to_check, seen_nums):    
    '''a recursive function for checking to see if the number passed
    in is happy or sad.  Keep a list of seen numbers because if a
    seen number is seen again, the number must be sad, as well as all
    the numbers that came before it.  If the number equals 1, the number
    is happy as well as all the numbers the came before it. Return True 
    if happy, return False if sad.'''
    
    #add the new number to seen_nums list
    seen_nums.append(number_to_check)
    
    #convert number to string to take each indiviual digit
    str_num = str(number_to_check)
        
    #initialize our next number to 0
    next_num = 0
    
    #iterate over the length of the number's digits
    for i in range(len(str_num)):
        #('digit ' + str(i) + ' is ' + (str_num[i])) --helpful for debug          
        #square each individual digit and add to the previous
        next_num += int(str_num[i])**2
        
    #print('next_number is ' + str(next_num)) -- helpful for debug
    #if the number is 1 or it is contained in the happy number list, return True
    if next_num == 1 or next_num in happy_nums:
        return True
    else:
        #if the number is contained in the seen list or the sad list, return False
        if next_num in seen_nums or next_num in sad_nums:
            return False
        
        #if number doesn't match either condition, recursively run function
        return happyLoop(next_num, seen_nums)
        
def getFromUser():
    '''prompt user for an interger and return the number as an interger'''
    
    return eval(input('Please enter a number, any number... (Integers Only!)'))

#intialize the lists that keep the happy, sad, and prime numbers
sad_nums = []
happy_nums = []
prime_nums = []

#set a max_num variable for only running primes_sieve when it needs to
max_num = 0      

#endless loop
while(True):
    #get the number to check
    number_to_check = getFromUser()
    
    #only get the prime numbers if not already contained in the prime_nums list
    if number_to_check > max_num:
        prime_nums = primes_sieve(number_to_check+1)
        max_num = number_to_check
        
    #only run happyLoop() when number is not defined
    if numberDefinition(number_to_check):
        #initalize empty seen_nums list
        seen_nums = []
        
        #if happyLoop() returns True, add the seen_nums to happy_nums list
        if happyLoop(number_to_check, seen_nums):
            happy_nums.extend(seen_nums)
            #prevent duplicates
            happy_nums = list(set(happy_nums))
        else:
        #if happyLoop() returns False, add the seen_nums to sad_nums list    
            sad_nums.extend(seen_nums)
            #prevent duplicates
            sad_nums = list(set(sad_nums))
        numberDefinition(number_to_check)

