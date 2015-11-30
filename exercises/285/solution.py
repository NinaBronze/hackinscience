import requests
try:
    r = requests.get('http://mdk.fr/ip')
    print(r)
except requests.exceptions.ConnectionError:
    print("No internet connectivity.")
