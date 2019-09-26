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


TODO vérifier que tab_list est bien un liste, verifier qu'il n'y est pas que des négatifs ou en tout cas pas diviser pa 0
'''
import numpy as np


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




tab_list=[1, 2, 3, -4, 6, -9]
tab_fromList=np.array(tab_list)

print('La moyenne est de :', average_above_zero(tab_list))
print('La plus grande valeur et son index sont :', max_value(tab_list))

        
        


