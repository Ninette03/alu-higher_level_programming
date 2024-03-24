#!/usr/bin/python3
""" Python script that fetches https://alu-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        print('Body response:')
        print('\t- type: {}'.format(type(response.text)))
        print('\t- content: {}'.format(response.text))
    else:
        print('Error code: {}'.format(response.status_code))
