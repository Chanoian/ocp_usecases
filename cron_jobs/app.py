import requests
import logging

def main():
    # Configure the logging format and level
    logging.basicConfig(level=logging.INFO)
    response = requests.get('https://google.com')
    if response.status_code == 200:
        logging.info('Request Was Successful !!')
    else:
        logging.info(f'Error: {response.status_code}')

if __name__ == '__main__':
    main()