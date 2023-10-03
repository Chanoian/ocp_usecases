import requests
import logging

def main():
    response = requests.get('https://google.com')
    if response.status_code == 200:
        logging.debug('Request Was Successful !!')
    else:
        logging.debug(f'Error: {response.status_code}')

if __name__ == '__main__':
    main()