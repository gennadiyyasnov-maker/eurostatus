import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(
    'https://api.github.com/user/repos',
    data=json.dumps({"name": "eurostatus-web", "private": True}).encode('utf-8'),
    headers={
        'Authorization': 'token ghp_a04lhLGzGrjX5zkcCWpJiH472zDKbh2CXpKg',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Python'
    },
    method='POST'
)

try:
    with urllib.request.urlopen(req, context=ctx) as response:
        print(response.read().decode())
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} {e.reason}")
    print(e.read().decode())
