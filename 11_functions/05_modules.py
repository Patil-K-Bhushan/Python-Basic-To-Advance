import math
import os
import mymodule
import requests

print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)