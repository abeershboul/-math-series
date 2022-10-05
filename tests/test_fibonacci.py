import pytest
from math_series.series import fibonacci

def test_string():
     actual=fibonacci("hii")
     expected ="Plz Enter a Number"
     assert actual == expected

def test_postive():
     actual=fibonacci(-3)
     expected ="Plz enter a positive number"
     assert actual == expected


def test_zero():
     actual=fibonacci(0)
     expected =0
     assert actual == expected

def test_one():
    actual=fibonacci(1)
    expected = 1
    assert actual==expected  

def test_two():
    actual=fibonacci(2)
    expected = 1
    assert actual==expected

def test_three():
    actual=fibonacci(3)
    expected = 2
    assert actual==expected   
  

def test_fuor() :
     actual=fibonacci(4)
     expected = 3
     assert actual==expected

  
    