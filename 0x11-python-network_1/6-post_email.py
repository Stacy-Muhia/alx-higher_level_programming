#!/usr/bin/python3
"""
   Takes URL and email sends a POST request to the passed 
   URL with the email as a parameter, and finally 
   displays the body of the response.
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    r = requests.post(url, value)
    print(r.text)
