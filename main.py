import time
import hmac
import hashlib
import base64
from datetime import datetime, timezone
from dotenv import load_dotenv
import os


load_dotenv()



SECRET_KEY = os.getenv("ACCESS-PASSPHRASE")

print(SECRET_KEY)
# API credentials
api_key = os.getenv("ACCESS-KEY")
secret_key = os.getenv("ACCESS-SECRETKEY")
passphrase = os.getenv("ACCESS-PASSPHRASE")

# Parameters for the request
timestamp = datetime.now(timezone.utc).isoformat(timespec='milliseconds')  # Example; use the current UTC time
method = "POST"
path = "/api/v5/account/balance"
body = '{"currency":"BTC"}'  # JSON-stringified body

# Create the prehash string
prehash_string = f"{timestamp}{method}{path}{body}"

# Generate the HMAC SHA256 signature
signature = base64.b64encode(
    hmac.new(secret_key.encode(), prehash_string.encode(), hashlib.sha256).digest()
)

print("OK-ACCESS-SIGN:", signature.decode())
print(timestamp)
