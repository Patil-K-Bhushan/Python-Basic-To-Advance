import requests

r = requests.get('https://api.github.com/users/Patil-K-Bhushan')

with open("Bhushan.txt", "w") as f:
    f.write(r.text)