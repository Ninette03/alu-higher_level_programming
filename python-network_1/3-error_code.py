#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8) """

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Get URL from command-line argument
    url = sys.argv[1]

    try:
        # Send request to the URL
        with urllib.request.urlopen(url) as response:
            # Read the response body
            html = response.read()
            # Decode response body in utf-8
            decoded_html = html.decode("utf-8")
            # Print the decoded body
            print(decoded_html)
    except urllib.error.HTTPError as e:
        # If an HTTPError occurs, print the error code
        print("Error code: {}".format(e.code))
