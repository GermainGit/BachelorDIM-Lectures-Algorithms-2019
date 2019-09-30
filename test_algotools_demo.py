#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: alben
"""
import S1_algotools_teacherdemo as algotools
import pytest

def inc_(x):
    return x+1

def test_inc():
    assert inc_(4)==5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
        
