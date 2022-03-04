from math_series.series import fibonacci
from math_series.series import lucas
# test for cases ==> 
# case A : basic 
# case B : float
# case C : negative number 
# case D : string
# fibonacci ==>
""" 
"""
def test_fibonacci_5():
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