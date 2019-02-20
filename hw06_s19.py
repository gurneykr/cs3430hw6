#!/usr/bin/python

#############################################
# module: hw06_s19.py
# Krista Gurney
# A01671888
#############################################

# These are the imports I used to implement my 
# solutions. Modify them as you see fit but
# make sure all your imports are zipped in your
# submission.

import math
import numpy as np
import matplotlib.pyplot as plt

from const import const
from maker import make_prod, make_const, make_pwr, make_e_expr, make_plus, make_quot
from tof import tof
from deriv import deriv

## ************* Problem 1 ******************

def percent_retention_model(lmbda, a):
    #r(t) = (100-a)e^(-lmbda*t) + a
    assert isinstance(lmbda, const)
    assert isinstance(a, const)

    left = make_plus(make_const(100.0), make_prod(-1.0, a.get_val()))
    right = make_e_expr(make_prod(make_prod(-1.0, lmbda.get_val()), make_pwr('t', 1.0)))

    return make_plus(make_prod(left, right), a.get_val())

def plot_retention(lmbda, a, t0, t1):
    assert isinstance(lmbda, const)
    assert isinstance(a, const)
    assert isinstance(t0, const)
    assert isinstance(t1, const)
    # your code here
    pass

## ************* Problem 2 ******************


def spread_of_disease_model(p, t0, p0, t1, p1):
    assert isinstance(p, const) and isinstance(t0, const)
    assert isinstance(p0, const) and isinstance(t1, const)
    # find B
    B = (p.get_val() - p0.get_val())/()


def plot_spread_of_disease(p, t0, p0, t1, p1, tl, tu):
    assert isinstance(p, const) and isinstance(t0, const)
    assert isinstance(p0, const) and isinstance(t1, const)
    pass
    
## ************* Problem 3 ******************

def plot_plant_growth(m, t1, x1, t2, x2, tl, tu):
    assert isinstance(m, const) and isinstance(t1, const)
    assert isinstance(x1, const) and isinstance(t2, const)
    assert isinstance(x2, const) and isinstance(tl, const)
    assert isinstance(tu, const)
    # your code here
    pass

def plant_growth_model(m, t1, x1, t2, x2):
    assert isinstance(m, const) and isinstance(t1, const)
    assert isinstance(x1, const) and isinstance(x2, const)
    assert isinstance(x2, const)
    # your code here
    pass
                                      
## ************* Problem 4 ******************

def spread_of_news_model(p, k):
    assert isinstance(p, const) and isinstance(k, const)
    # your code here
    pass

def plot_spread_of_news(p, k, tl, tu):
    assert isinstance(p, const) and isinstance(k, const)
    assert isinstance(tl, const) and isinstance(tu, const)
    # your code here
    pass




 
