#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL
    displays the value of the variable X-Request-Id
"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    r = requests.get(url)

    print(r.headers.get("X-Request-Id"))
