import requests

res = requests.get("127.0.0.1:3000/api/__main__")
res = requests.get("127.0.0.1:3000/api/record/1")
res = requests.post("127.0.0.1:3000/user", {})
res = requests.post("127.0.0.1:3000/category", {})
res = requests.post("127.0.0.1:3000/record", {})
print(res.json)
