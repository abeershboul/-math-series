import pytest
from math_series.series import lucas

def test_string():
     actual=lucas("hii")
     expected ="Plz Enter a Number"
     assert actual == expected

def test_postive():
     actual=lucas(-3)
     expected ="Plz enter a positive number"
     assert actual == expected

def test_zero():
     actual=lucas(0)
     expected =2
     assert actual == expected

def test_one():
     actual=lucas(1)
     expected =1
     assert actual == expected

def test_two():
    actual=lucas(2)
    expected=3
    assert actual == expected

def test_three():
    actual=lucas(3)
    expected=4
    assert actual == expected


def test_four():
    actual=lucas(4)
    expected=7
    assert actual == expected        


   

