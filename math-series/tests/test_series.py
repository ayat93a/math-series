from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series
# test for cases ==> 
# case A : basic 
# case B : float
# case C : negative number 
# case D : string
# fibonacci ==>
""" 
"""
def test_fibonacci_0():
    actual = fibonacci(0)
    expected =  0
    assert actual == expected

def test_fibonacci_1():
    actual = fibonacci(1)
    expected =  1
    assert actual == expected

def test_fibonacci_2():
    actual = fibonacci(2)
    expected =  2
    assert actual == expected

def test_fibonacci_2():
    actual = fibonacci(5)
    expected =  5
    assert actual == expected

# def test_fibonacci_float():
#     actual = fibonacci (1.5)
#     expected = 'fibonacci function accept only integer numbers'
#     assert actual == expected

# def test_fibonacci_neg():
#     actual = fibonacci (-1)
#     expected = 'fibonacci function accept only integer numbers'
#     assert actual == expected 

# def test_fibonacci_str():
#     actual = fibonacci('a')
#     expected = 'fibonacci function accept only integer numbers'
#     assert actual == expected 
    
# lucas
def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected 

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected 


def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected 

# def lucas_float ():
#     actual = lucas(0.5)
#     expected = 'lucas function accepts only integer number'
#     assert actual == expected

# def lucas_neg ():
#     actual = lucas(-5)
#     expected = 'lucas function accepts only integer number'
#     assert actual == expected 

# def lucas_str():
#     actual = lucas('a')
#     expected = 'lucas function accept only integer numbers'
#     assert actual == expected

#sum
def test_sum_series0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected 

def test_sum_series1():
    actual = sum_series(1)
    expected = 1
    assert actual == expected 

def test_sum_series5():
    actual = sum_series(5)
    expected = 5
    assert actual == expected 

