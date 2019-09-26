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
import numpy as np

tab_list=[1, 2, 3, -4, 6, -9]
tab_fromList=np.array(tab_list)


def average_above_zero(tab_fromList):
    som=0
    nbOfPositives=0
    
    for id in range(len(tab_fromList)):
    
        if tab_fromList[id] > 0:
            som=som+tab_fromList[id]
            nbOfPositives+=1
   
    return som / nbOfPositives



print('La moyenne est de :', average_above_zero(tab_list))

        
        


