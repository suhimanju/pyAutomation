"""
This Scripts sends request to url and prints the response status and response body

Here we are using the python's requests module to make a call to the REST end point

Install the requests module using "pip install requests"
"""

import requests

resp = requests.get("http://www.thomasbayer.com/sqlrest/CUSTOMER/")
print("The status code is: %d" % resp.status_code + "\n")

if resp.status_code == requests.codes.ok:
    print("Print the body of url")
    print(resp.text)
