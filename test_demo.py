import pytest
import demo

def test_add():
# GIVEN two numbers
# WHEN I invoke the method
# THEN I get the addition of two numbers
    add_result = demo.add(3,4)
    assert add_result == 7
    assert demo.add(1,10) == 11
    assert demo.add(2,4) == 6

def test_sub():
# GIVEN two numbers
# WHEN I invoke the method
# THEN I get the addition of two numbers
    assert demo.sub(3,4) == -1
    assert demo.sub(1,9) == -8
    assert demo.sub(2,4) == -2


