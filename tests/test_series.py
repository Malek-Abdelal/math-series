import pytest
import series.series 

#fibonacci tests
def test_fibonacci_0():                   
    actual = series.series.fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_1():
    actual = series.series.fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_2():
    actual = series.series.fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_3():
    actual = series.series.fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_5():
    actual = series.series.fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_9():
    actual = series.series.fibonacci(9)
    expected = 34
    assert actual == expected

#lucas tests
def test_lucas_0():
    actual = series.series.lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = series.series.lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_2():
    actual = series.series.lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_6():
    actual = series.series.lucas(6)
    expected = 18
    assert actual == expected

def test_lucas_11():
    actual = series.series.lucas(11)
    expected = 199
    assert actual == expected
    

