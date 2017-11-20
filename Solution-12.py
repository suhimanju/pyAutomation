"""Write a program that can parse a JSON string {a:1,b:2,c:3} and print the keys and values. Then
access the value 3 using its key ‘c’."""

import json

json_input = '{"a":1,"b":2,"c":3}'

try:
    data = json.loads(json_input)

    #printing json-formatted string
    print(json.dumps(data, sort_keys=True, indent=4))

    print("Accessing Json data using its key 'c': ",data['c'])


except(ValueError,KeyError,TypeError,UnicodeDecodeError):
    print("Error in JSON format")
    
