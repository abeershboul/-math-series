import pytest
from math_series.series import sum_series

def test_string():
     actual=sum_series("hii")
     expected ="Plz Enter a Number"
     assert actual == expected

def test_postive():
     actual=sum_series(-3)
     expected ="Plz enter a positive number"
     assert actual == expected     

def test_zero():
     actual=sum_series(0)
     expected =0
     assert actual == expected
def test_one():
     actual=sum_series(1)
     expected =1
     assert actual == expected

def test_two():
     actual=sum_series(2)
     expected =1
     assert actual == expected 


    

def test_three():
     actual=sum_series(3)
     expected =2
     assert actual == expected 

def test_four():
     actual=sum_series(4,2,3)
     expected =13
     assert actual == expected 

def test_random():
    actual=sum_series(1,4,5)
    expected=5
    assert actual == expected     





