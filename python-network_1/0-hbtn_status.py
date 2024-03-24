#!/usr/bin/python3
""" Python script that fetches https://alu-intranet.hbtn.io/status """
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf-8")
            print('Body response:')
            print('\t- type: {}'.format(type(html)))
            print('\t- content: {}'.format(html))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
