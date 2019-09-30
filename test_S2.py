# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:47:49 2019

@author: PREVOT Germain
"""

import S1_algotools_teacherdemo as algotools
import pytest

        
def test_average_above_zero_working1():
    tab_list=[1, 2, 3, -4, 6, -9]
    test, lastID= algotools.average_above_zero(tab_list)
    assert test == 3
    
def test_average_above_zero_listInput():
    tab_list="salut"
    with pytest.raises(TypeError):
        test, lastID=algotools.average_above_zero(tab_list)
        
def test_average_above_zero_divideZero():
	tab_list=[-1,-2,-3,-4,-6,-9]
	with pytest.raises(ZeroDivisionError):
		test, lastID=algotools.average_above_zero(tab_list)
        
def test_average_above_zero_notEmpty():
    tab_list=[]
    with pytest.raises(ValueError):
        test, lastID=algotools.average_above_zero(tab_list)

def test_average_above_zero_onlyNumbers():
    tab_list=["test"]
    with pytest.raises(ValueError):
        test, lastID=algotools.average_above_zero(tab_list)