import json

# f = open("data.json", "r")
# content = f.read()
# print(content)
# f.close()

import json
with open("data.json", "r") as f:
data = json.load(f)
print(data)

import os
os.remove("data.json")