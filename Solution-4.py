"""
A class method that adds two numbers x and y

Note: The script uses pytest to perform tests the add method. Please install pytest using "pip install pytest"
      Execute the test cases using "pytest" command from the command prompt as below:
      pytest -v Solution-4.py

      In normal execution without using pytest, the script will execute add method and print the sum.
"""

import pytest

class Addition(object):
    #Initialization of class variables x,y
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #Class method sum that performs the adds the two numbers
    def add(self):
        total = sum([self.x,self.y])
        return total

# test to compare sums of one pair numbers is greater than the other 
def test_greater():
    s1 = Addition(10,15)
    s2 = Addition(20,1)
    a1 = s1.add()
    a2 = s2.add()
    assert a1 > a2

# test to compare sums of one pair numbers is less than the other 
def test_lesser():
    s1 = Addition(10,15)
    s2 = Addition(20,6)
    a1 = s1.add()
    a2 = s2.add()
    assert a1 < a2

# test to compare sums of one pair numbers is equal than the other 
def test_equal():
    s1 = Addition(50,10)
    s2 = Addition(30,30)
    a1 = s1.add()
    a2 = s2.add()
    assert a1 == a2

# test that adds two negative integers
def test_add_negInt(): 
    s1 = Addition(-50,-10)
    a1 = s1.add()
    assert a1 < 0
    
#test that adds a positive and a negetive checks if sum is greater than 0
#Using Marker xfail() as the test can be expected to fail based on input
@pytest.mark.xfail()
def test_add_neg_and_pos_Int():
    s1 = Addition(50,-10)
    a1 = s1.add()
    assert a1 > 0

if __name__ == '__main__':
    a = Addition(10,30.0)
    b = a.add()
    print("The sum of numbers is: %d" % b)
