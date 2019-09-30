# -*- coding: utf-8 -*-
"""
Éditeur PREVOT Germain
Exerice algo DIM
"""

'''
What happens if Som initialization is forgotten ?

----- It's depend of the language, but it'll work not corretly with random values.

What can you expect if all the values are below zero ?

----- An error because we can't divid up by zero.

'''
import S1_algotools_teacherdemo as algotools
import pytest
import numpy as np

# =============================================================================
# Exercice n°1
# =============================================================================


def average_above_zero(tab_fromList):
    
    if not(isinstance(tab_fromList, list)):
        raise ValueError('average_above_zero expected a list as input')
    if len(tab_fromList) == 0:
        raise ValueError('average_above_zero expected a not empty list')
    if not(isinstance(tab_fromList[0], (int, float))):
        raise ValueError('average_above_zero expected a list of number')
        
    som=0
    nbOfPositives=0
    
    for id in range(len(tab_fromList)):
    
        if tab_fromList[id] > 0:
            som=som+tab_fromList[id]
            nbOfPositives+=1
    if nbOfPositives != 0:
        return som / nbOfPositives
    else:
        raise ValueError('average_above_zero expected positive number')

# =============================================================================
# Exercice n°2
# =============================================================================
        
def max_value(tab_fromList):
    
    if not(isinstance(tab_fromList, list)):
        raise ValueError('average_above_zero expected a list as input')
    if len(tab_fromList) == 0:
        raise ValueError('average_above_zero expected a not empty list')
    if not(isinstance(tab_fromList[0], (int, float))):
        raise ValueError('average_above_zero expected a list of number')
        
    maxVal=0
    maxId=0

    for id in range(len(tab_fromList)):
        compareVal=tab_fromList[id-1]
        if compareVal > tab_fromList[id]:
            maxVal = compareVal
            maxId = id-1
        
    return float(maxVal), int(maxId)

# =============================================================================
# Exercice n°3
# =============================================================================

def reverse_table(tab_fromList):
    
    if not(isinstance(tab_fromList, list)):
        raise ValueError('average_above_zero expected a list as input')
    if len(tab_fromList) == 0:
        raise ValueError('average_above_zero expected a not empty list')
    if not(isinstance(tab_fromList[0], (int, float))):
        raise ValueError('average_above_zero expected a list of number')
    tab_len=len(tab_fromList)
    for id in range(len(tab_fromList)):
        memVal = tab_fromList[tab_len-1]
        tab_fromList.pop(tab_len-1)    
        tab_fromList.insert(id, memVal)
    
    return tab_fromList

# =============================================================================
# Exercice n°4
# =============================================================================
import cv2

def roi_bbox(matrix):
    
    minCol=matrix.shape[1]
    minRow=matrix.shape[0]
    maxCol=0
    maxRow=0
    
    for idrow in range(matrix.shape[0]):
        for idcol in range(matrix.shape[1]):            
            pixVal=matrix[idrow, idcol]
            if pixVal == 255:
                if idrow > maxRow:
                    maxRow=idrow
                if idcol > maxCol:
                    maxCol=idcol
                if idcol < minCol:
                    minCol = idcol
                if idrow < minRow:
                    minRow = idrow
    result=np.array([[minCol, minRow], [maxCol, minRow], [minCol, maxRow], [maxCol, maxRow]])
    return result        
    
    
# =============================================================================
#   Premiere idee, pour forme rectangulaire
#     for idrow in range(matrix.shape[0]):
#         for idcol in range(matrix.shape[1]):            
#             pixVal=matrix[idrow, idcol]
#             if pixVal == 1:
#                 preVal=matrix[idrow, idcol-1]
#                 postVal=matrix[idrow, idcol+1]
#                 checkRowUp=matrix[idrow-1, idcol]
#                 checkRowDown=matrix[idrow+1, idcol]
#                 
#                 if preVal == 0 or postVal==0:
#                     if checkRowUp != 1 or checkRowDown !=1:
#                         print(idcol, idrow)
#           #Atendu : 4 3 / 7 3 / 4 5 / 7 5   
# =============================================================================
                


img = cv2.imread('img.png',0)

tab_list =[1, 2, 3, -4, 6, -9]
tab_fromList=np.array(tab_list)


    
print('La moyenne est de :', average_above_zero(tab_list))
print('La plus grande valeur et son index sont :', max_value(tab_list))
print('Le tableau inversé est :', reverse_table(tab_list))
print('Bounding result :', roi_bbox(img))
