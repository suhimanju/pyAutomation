"""
Program to parse an integer array and verify that it is a valid SSN number
"""

"""
Rules for SSN number:

^                           #Start of expression
(?!219-09-9999|078-05-1120) #Don't allow "219-09-999" or "078-05-1120" explicitly
(?!666|000|9\d{2})\d{3}     #Don't allow the SSN to begin with 666, 000 or anything between 900-999
-                           #Explicit dash (separating Area and Group numbers)
(?!00)\d{2}                 #Don't allow the Group Number to be "00"
-                           #Another dash (separating Group and Serial numbers)
(?!0{4})\d{4}               #Don't allow last four digits to be "0000"
$                           #End of expression
"""

import re

pattern = re.compile(r'^(?!219-09-9999|078-05-1120)(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}$')

def match_ssn(ssn_number):

    # Match the pattern against user input
    if(re.match(pattern,ssn_number)):
        print(ssn_number + ": is a valid SSN number")

    else:
        print(ssn_number + ": is not a valid SSN Number")

match_ssn("123-45-6789")
match_ssn("123-45-67")

