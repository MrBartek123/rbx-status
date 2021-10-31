import requests
try:
    r = requests.head("https://roblox.com")
    print(r.status_code)
    if r.status_code == 503:
      json = {"status": ":("}
    # prints the int of the status code. Find more at httpstatusrappers.com :)
except requests.ConnectionError:
    print("failed to connect")
