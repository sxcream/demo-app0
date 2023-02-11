import requests

r = requests.get('http://www.exemple.com')
print(r.status_code)