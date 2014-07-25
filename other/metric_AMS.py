# -*- coding: utf-8 -*-
"""
Evaluation metric for the Higgs Boson Kaggle Competition,
as described on:
https://www.kaggle.com/c/higgs-boson/details/evaluation

@author: Joyce Noah-Vanhoukce
Created: Thu Apr 24 2014
"""

import os
import csv
import math


def create_solution_dictionary(solution):
    """ Read solution file, return a dictionary with key EventId and value (label, weight).
    Solution file headers: EventId, Label, Weight """
    
    solnDict = {}
    with open(solution, 'rb') as f:
        soln = csv.reader(f)
        soln.next() # header
        for row in soln:
            if row[0] not in solnDict:
                solnDict[row[0]] = (row[1], row[2])
    return solnDict

        
def check_submission(submission, Nelements):
    """ Check that submission RankOrder column is correct:
        1. All numbers are in [1,NTestSet]
        2. All numbers are unqiue
    """
    rankOrderSet = set()    
    with open(submission, 'rb') as f:
        sub = csv.reader(f)
        sub.next() # header
        for row in sub:
            rankOrderSet.add(int(row[1]))
            
    if len(rankOrderSet) != Nelements:
        print 'RankOrder column must contain unique values'
        return False
    elif rankOrderSet.issubset(set(xrange(1,Nelements+1))) == False:
        print 'RankOrder column must contain all numbers from [1..NTestSset]'
        return False
    else:
        return True

    
def AMS(s, b, br=10.0):
    """ Approximate Median Significance defined as:
        AMS = sqrt(
                2 { (s + b + b_r) log[1 + (s/(b+b_r))] - s}
              )        
    where b_r = 10, b = background, s = signal, log is natural logarithm """
    
    radicand = 2 * ( (s+b+br) * math.log (1.0 + s / (b+br)) - s )
    if radicand < 0:
        print 'radicand is negative. Exiting'
        return 0
    else:
        return math.sqrt(radicand)


def AMS_metric(solution, submission):
    """  Prints the AMS metric value to screen.
    Solution File header: EventId, Class, Weight
    Submission File header: EventId, RankOrder, Class
    """
    
    
    # solutionDict: key=eventId, value=(label, class)
    solutionDict = create_solution_dictionary(solution)
    numEvents = len(solutionDict) # number of events = size of test set
    print numEvents 

    signal = 0.0
    background = 0.0
    if check_submission(submission, numEvents):
        with open(submission, 'rb') as f:
            sub = csv.reader(f)
            sub.next() # header row
            for row in sub:
                if row[2] == 's': # only events predicted to be signal are scored
                    if row[0] not in solutionDict:
                        print 'EventId %s is not in solutionDict' % row[0]
                        return 0
                    if solutionDict[row[0]][0] == 's':
                        signal += float(solutionDict[row[0]][1])
                    elif solutionDict[row[0]][0] == 'b':
                        background += float(solutionDict[row[0]][1])
     
        print 'signal = {0}, background = {1}'.format(signal, background)
        ams = AMS(signal, background)
        print 'AMS = ' + str(ams)
        return ams 
    return 0


if __name__ == "__main__":

    solutionFile = ""
    submissionFile = ""
    import sys
    if len(sys.argv) < 3:
        print '<usage> solution submission'
        exit(-1)
    solutionFile = sys.argv[1]
    submissionFile = sys.argv[2]
    
    AMS_metric(solutionFile, submissionFile)
    
    
