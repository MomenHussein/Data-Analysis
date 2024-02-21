import numpy as np
def addition(a=[],b=[]):
    if len(a) == len(b):
        return a+b
    else:
        return "Sorry invalid dimensions"

def sunbstraction(a=[],b=[]):
    if len(a) == len(b):
        return a-b
    else:
        return "Sorry invalid dimensions"

def scalmultiplication(a=[],b=[]):
    if len(a) == len(b):
        return a*b

def scaldivision(a=[],b=[]):
    if len(a) == len(b):
        return a/b

def scalnummultiplication(a=[],num):
    if len(a) == len(b):
        return a*num
        
def scalnumdivision(a=[],num):
    if len(a) == len(b):
        return a/num
    
def dotmultiplication(a=[],b=[]):
    
    dimensions1 = np.shape(a)
    rows1, columns1 = dimensions1
    dimensions2 = np.shape(b)
    rows2, columns2 = dimensions2
 
    res = [[0 for x in range(rows1)] for y in range(columns2)] 
 
# explicit for loops
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
 
            # resulted matrix
                res[i][j] += a[i][k] * b[k][j]
    
    return res

def inverse(a=[]):

    return np.linalg.inv(a)

def division(a=[],b=[]):
    arr1 = inverse(b)
    arr2 = dotmultiplication(a,arr1)
    return arr2

def transpose(arr=[]):
    print(list(map(list, zip(*arr))))