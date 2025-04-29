import os
import sys  # unused import

def flattenNestedList(input):
    flat_list = []
    for i in range(len(input)):
        if input[i] != []:
            for j in range(len(input[i])):
                flat_list.append(input[i][j])
    return flat_list

def getLastElement(list):
    return list[-1] if len(list) > 0 else None  # missing error handling, unclear name

def calcAverage(l):
    total = 0
    for x in l:
        total += x
    return total / len(l)  # no zero division check