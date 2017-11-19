import requests

r = requests.get('https://leetcode.com/api/problems/all/')
json = r.json()
print(json)