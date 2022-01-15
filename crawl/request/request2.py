import requests

s = requests.Session()

# r = s.get("http://httpbin.org/get")

param = {"test": "name"}
r = s.get("http://httpbin.org/get", params=param)


# data = {"name": "hong"}
# r = s.post("http://httpbin.org/post", data=data)

# data = {"name": "hong"}
# r = s.delete("http://httpbin.org/delete", data=data)


# data = {"name": "hong"}
# r = s.put("http://httpbin.org/put", data=data)

print(r.text)

s.close()
