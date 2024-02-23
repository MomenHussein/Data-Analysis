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

def scalnummultiplication(a=[],num=1):
    for i in range(len(a)):
        a[i]*=num
    return a
        
def scalnumdivision(a=[],num=1):
    for i in range(len(a)):
        a[i]/=num
    return a

def scalnumadd(a=[],num=0):
    for i in range(len(a)):
        a[i]+=num
    return a

def scalnumsubstraction(a=[],num=0):
    for i in range(len(a)):
        a[i]-=num
    return a
    
def dotmultiplication(mat1=[[]],mat2=[[]]):
    
    dimensions1 = np.shape(mat1)
    R1, C1 = dimensions1
    dimensions2 = np.shape(mat2)
    R2, C2 = dimensions2
    if C1 == R2:
        res = [[0 for x in range(R1)] for y in range(C2)] 
     
    # explicit for loops
        for i in range(0, R1):
            for j in range(0, C2):
                for k in range(0, R2):
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res
    else:
        return "Sorry Invalid Dimensions"
    
        

def inverse(a=[]):

    return np.linalg.inv(a)

def division(a=[],b=[]):
    arr1 = inverse(b)
    arr2 = dotmultiplication(a,arr1)
    return arr2

def transpose(arr=[]):
    print(list(map(list, zip(*arr))))
    
print(dotmultiplication([[1, 2, 3],[3, 4, 5],[7, 6, 4]],[[5, 2, 6],[5, 6, 7],[7, 6, 4]]))
                                     
                                     
   
    
