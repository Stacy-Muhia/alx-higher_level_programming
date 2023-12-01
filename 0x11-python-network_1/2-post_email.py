#!/usr/bin/python3
"""
   takes in a URL and an email, sends a POST request to the passed URL
   and displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
