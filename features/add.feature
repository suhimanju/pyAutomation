Feature: Basic arithmetic
  In order to produce the correct answer
  I want to call the correct method the users requests
 
 Scenario: Adding two numbers
   Given the user selects addition
   When the user provides the numbers 3 and 4
   Then the result should equal 7