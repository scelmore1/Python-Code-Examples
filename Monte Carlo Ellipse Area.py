# -*- coding: utf-8 -*-
"""
DSC 430 Assignment 0702

Scott Elmore
11/04/19

 “I have not given or received any
unauthorized assistance on this assignment”


YouTube Link : https://youtu.be/ExvG1RY5V5s
"""

import math
from DSC430_A0701 import WarAndPeacePseudoRandomNumberGenerator


class Point:
    '''represents an X,Y point'''
    
    def __init__(self, x, y):
        'intialize by passing an x and y'
        self.x = x
        self.y = y
        
    def __repr__(self):
        'when called, return a string Point(x,y)'
        return self.__class__.__name__ + '(' + str(self.x) + ', ' + str(self.y) + ')'
        
    def getCoordinates(self):
        'return coordinates as a tuple of (x,y)'
        return (self.x, self.y)
        
class Ellipse:
    '''represents an ellipse containing two points and a long axis width'''
    
    def __init__(self, point1, point2, width_la):   
        'initialize by passing in two points and a long axis width'
        self.point1 = point1
        self.point2 = point2
        self.width_la = width_la
        
        #get the point coordinates and determine the overall min and max x and y coordinates
        p1 = self.point1.getCoordinates()
        p2 = self.point2.getCoordinates()
        if p1[0] < p2[0]:
            self.minX = p1[0]
            self.maxX = p2[0]
        else:
            self.minX = p2[0]
            self.maxX = p1[0]
        if p1[1] < p2[1]:
            self.minY = p1[1]
            self.maxY = p2[1]
        else:
            self.minY = p2[1]
            self.maxY = p1[1]   
            
    def __repr__(self):
        'when called, return a string Ellipse(Point1, Point2, Width)'
        return self.__class__.__name__ + '(' + str(self.getP1()) + ', ' + str(self.getP2()) + ', ' \
        + str(self.getWidthLA()) + ')'
            
    def getP1(self):
        'return point1'
        return self.point1
    
    def getP2(self):
        'return point2'
        return self.point2
    
    def getWidthLA(self):
        'return long axis width'
        return self.width_la
    
    def getMinX(self):
        'return overall minumum X coordinate'
        return self.minX
    
    def getMaxX(self):
        'return overall maximum X coordinate'
        return self.maxX
    
    def getMinY(self):
        'return overall minumum Y coordinate'
        return self.minY
    
    def getMaxY(self):
        'return overall maximum Y coordinate'
        return self.maxY

def getBoundaries(ellipse1, ellipse2):
    '''determine boundaries of which the two ellipses must be contained within'''
    e1_la = ellipse1.getWidthLA()
    e2_la = ellipse2.getWidthLA()

    #determine the boundaries using the min and max coordinates subtracting the maximum long axis
    #width divided by 2
    left_bound = min(ellipse1.getMinX(), ellipse2.getMinX()) - (max(e1_la, e2_la) / 2)
    right_bound = max(ellipse1.getMaxX(), ellipse2.getMaxX()) + (max(e1_la, e2_la) / 2)
    lower_bound = min(ellipse1.getMinY(), ellipse2.getMinY()) - (max(e1_la, e2_la) / 2)
    upper_bound = max(ellipse1.getMaxY(), ellipse2.getMaxY()) + (max(e1_la, e2_la) / 2)

    #calculate length, height, and the origin of the rectangle
    length = right_bound - left_bound
    height = upper_bound - lower_bound
    origin = (left_bound, lower_bound)
    return length, height, origin
  
def getModifiedNumber(rand_num, multiplier, shifter):
    '''get the modified random number calculated by multiplying and shifting'''
    return (rand_num * multiplier) + shifter
    

def isInEllipse(ellipse, rand_point):
    '''determine if the rand_point is contained in the ellipse'''
    #get coordinates for all relevant points
    rand_coord = rand_point.getCoordinates()
    p1_coord = ellipse.getP1().getCoordinates()
    p2_coord = ellipse.getP2().getCoordinates()
    
    #get the distance of the random point to the two ellipse points
    dist_1 = math.sqrt((rand_coord[0] - p1_coord[0])**2 + (rand_coord[1] - p1_coord[1])**2)
    dist_2 = math.sqrt((rand_coord[0] - p2_coord[0])**2 + (rand_coord[1] - p2_coord[1])**2)
    
    #if the two distances sum to less than or equal long axis width, point is in ellipse
    return dist_1 + dist_2 <= ellipse.getWidthLA()
    
    
def computeOverlapOfEllipses(ellipse1, ellipse2):
    '''main loop for generating random numbers and determining if the random number
    is contained within the overlap of two ellipses'''
    
    boundaries = getBoundaries(ellipse1, ellipse2)
    prng = WarAndPeacePseudoRandomNumberGenerator(300)
    
    #keep count of the number of points that are within both ellipses
    area_counter = 0
    
    #iterate through the number of iterations to generate random points
    for i in range(num_iterations):
        r = prng.random()
        x = getModifiedNumber(r, boundaries[0], boundaries[2][0])
        r = prng.random()
        y = getModifiedNumber(r, boundaries[1], boundaries[2][1])
        check_e1 = isInEllipse(ellipse1, Point(x,y))
        check_e2 = isInEllipse(ellipse2, Point(x,y))
        #point is contained in both ellipses
        if check_e1 and check_e2:
#            print('\n{} In Area'.format(Point(x,y)))
            area_counter += 1
    
    #calculate area by getting rectangle area and multiplying the fraction
    #of times the points are contained within both ellipses
    boundary_area = boundaries[0] * boundaries[1]
    area = (area_counter / num_iterations) * boundary_area 
    
    return area


def Main():
    '''generate points and ellipses to determine overlap area'''
    
    p1 = Point(2, 3)
    p2 = Point(4, 3)   
    e1 = Ellipse(p1, p2, 4)   
    p3 = Point(5, 3)   
    e2 = Ellipse(p2, p3, 3)   
    overlap = computeOverlapOfEllipses(e1, e2)
   
    print('\nEstimated area under overlap of two ellipses, {} & {}, is {}:'.format(e1, e2, overlap))
    
    p1 = Point(0, 0)  
    e1 = Ellipse(p1, p1, 2)      
    e2 = Ellipse(p1, p1, 2)  
    overlap = computeOverlapOfEllipses(e1, e2)
    
    print('\nEstimated area under overlap of two ellipses, {} & {}, is {}:'.format(e1, e2, overlap))
    
    p1 = Point(-10, -124)
    p2 = Point(432, 123)
    p3 = Point(-142, 4)
    p4 = Point(99, 525)
    e1 = Ellipse(p1, p2, 700)      
    e2 = Ellipse(p3, p4, 800)  
    overlap = computeOverlapOfEllipses(e1, e2)
    
    print('\nEstimated area under overlap of two ellipses, {} & {}, is {}:'.format(e1, e2, overlap))
    
    p1 = Point(0, 5)
    p2 = Point(0, 4)
    p3 = Point(3, 5)
    p4 = Point(3, 4)
    e1 = Ellipse(p1, p2, 3)      
    e2 = Ellipse(p3, p4, 3)  
    overlap = computeOverlapOfEllipses(e1, e2)
    
    print('\nEstimated area under overlap of two ellipses, {} & {}, is {}:'.format(e1, e2, overlap))    

num_iterations = 10000
Main()