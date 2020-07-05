import requests
r = requests.get("https://qpi.github.com/iser", auth=("user", "pass"))
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json