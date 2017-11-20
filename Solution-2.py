"""
String Reversal Program
"""

def string_Reverse(data):
    """Since there is no built-in reverse method for str data type in python, we can reverse a python string
    by slicing from the last index of an input string which starts at -1 till the beginning of the string"""
    print("The input string before reversal is: " + data)
    print("The reversed string of the input is: " + data[::-1])

string_Reverse("abcdef")
