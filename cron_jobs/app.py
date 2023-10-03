import requests

def main():
    response = requests.get('https://google.com')
    if response.status_code == 200:
        print ('Request Was Successful !!')
    else:
        print(f'Error: {response.status_code}')

if __name__ == '__main__':
    main()