"""
This script is using BDD: Behavioral Driven Development and is using python's behave framework

Pre-Requisites:
1. In order to execute this script we need to install "behave" third-party module as below:
pip install behave

2. Make sure that your script path has a feature file "add.feature" within "features" directory

3. Make sure that your test script is in steps directory

4. Execute this script from the steps path using "behave" command in the prompt
"""

#Importing behave module
from behave import *

@given(u'the user selects addition')
def given_addition(context):
    context.method = sum
 
@when(u'the user provides the numbers 3 and 4')
def when_numbers(context):
    context.result = context.method([3,4])
 
@then(u'the result should equal 7')
def then_equal(context):
    assert context.result == 7
