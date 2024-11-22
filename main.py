import time
import hmac
import hashlib
import base64
from datetime import datetime, timezone
from dotenv import load_dotenv
import os
import requests


load_dotenv()



SECRET_KEY = os.getenv("ACCESS-PASSPHRASE")

print(SECRET_KEY)
# API credentials
api_key = os.getenv("ACCESS-KEY")
secret_key = os.getenv("ACCESS-SECRETKEY")
passphrase = os.getenv("ACCESS-PASSPHRASE")

# Endpoint and request details
base_url = "https://www.okx.com"
endpoint = "/api/v5/account/bills?type=1&limit=100"
url = base_url + endpoint
method = "GET"

# Generate timestamp in ISO 8601 format
timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")



# Generate the HMAC SHA256 signature
#signature = base64.b64encode(
#    hmac.new(secret_key.encode(), prehash_string.encode(), hashlib.sha256).digest()
#)
# Prehash string: combine the timestamp, HTTP method, and request path
prehash_string = f"{timestamp}{method}{endpoint}"
signature = base64.b64encode(
    hmac.new(secret_key.encode(), prehash_string.encode(), digestmod="sha256").digest()
)



# HTTP headers
headers = {
    "OK-ACCESS-KEY": api_key,
    "OK-ACCESS-SIGN": signature.decode(),
    "OK-ACCESS-TIMESTAMP": timestamp,
    "OK-ACCESS-PASSPHRASE": passphrase,
    "Content-Type": "application/json",
}

# Make the GET request
response = requests.get(url, headers=headers)

# Print the response
print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())

#print("OK-ACCESS-SIGN:", signature.decode())
#print(timestamp)
