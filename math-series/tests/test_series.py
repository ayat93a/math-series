from math_series.series import fibonacci,lucas
# test for cases ==> 
# case A : basic 
# case B : float
# case C : negative number 

# fibonacci ==>
""" 
"""
def test_fibonacci_5():
    actual = fibonacci(5)
    expected =  5
    assert actual == expected

def test_fibonacci_float():
    actual = fibonacci (1.5)
    expected = 'fibonacci function accept only numbers'
    assert actual == expected

def test_fibonacci_neg():
    actual = fibonacci (-1)
    expected = 'fibonacci function accept only numbers'
    assert actual == expected 

# lucas
def lucas_5():
    actual = lucas(5)
    expected = 5
    assert actual == expected 

def lucas_float ():
    actual = lucas(0.5)
    expected = 'lucas function accepts only number'
    assert actual == expected

def lucas_neg ():
    actual = lucas(-5)
    expected = 'lucas function accepts only number'
    assert actual == expected 