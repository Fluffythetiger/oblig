#import datetime
from main import*

import pytest

y = 400
y1 = 100
y2 = 333
y3 = 20


# test Code main.py
# leap year
def test_divisble_on4():
   assert is_it_divisible_on_4(y) == True

def test_divisible_on_100():
    assert is_divisible_100(y) == True

def test_divisible_on_400():
    assert is_it_divisible_on_400(y) == True

# not leap year
def test_is_it_not_divisible_4():
    assert is_it_not_divisible_4(y2) == False

def test_is_divisible_100():
    assert not_divisible_on_100(y2) == True

def test_not_divisible_on_400():
    assert not_divisible_on_400(y2) == True

# multi


def test_is_leap():
    assert see_if_leepYear(y) == True


def test_not_leap():
    assert see_if_leepYear(y2) == False

def test_isLeapYear_give_true():
    isLeapYear(y) == True

def test_isLeapYear_give_false():
    isLeapYear(y2) == False

# test logic
# leep year
def test_is_it_divisible_on_4():
    s = y%4 == 0
    assert s == True

def test_not_divisible_on_100():
    s = y2%100 == 0
    assert s == False

def test_is_it_divisible_on_400():
    s = y%400 == 0
    assert s == True


# not leap year
def test_is_it_not_divisible_4():
    s = y2%4 == 0
    assert s == False

def test_is_divisible_100():
    s = y1%100 == 0
    assert s == True

def test_not_divisible_on_400():
    s = y2%400 == 0
    assert s == False

# multi
def test_is_divisible_on_4_but_not_100():
    if (y3 % 4 == 0) and (y3 % 100 != 0):
      s = True
    else:
      s = False
    assert s == True

def test_is_leap():
    a = 2000
    if (a % 400 == 0):
        s = True
    elif (a % 4 == 0) and (a % 100 != 0):
        s = True
    else:
        s = False
    assert s == True

def test_not_leap():
    a = 1800
    if (a % 400 == 0):
        s = True
    elif (a % 4 == 0) and (a % 100 != 0):
        s = True
    else:
        s = False
    assert s == False



