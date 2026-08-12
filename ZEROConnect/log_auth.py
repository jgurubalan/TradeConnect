from kiteconnect import KiteConnect
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("KITE_API_KEY")
api_secret = os.getenv("KITE_API_SECRET")

kite = KiteConnect(api_key=api_key)

print("\nLogin here:")
print(kite.login_url())

request_token = input("\nPaste request token here: ").strip()

data = kite.generate_session(
    request_token,
    api_secret=api_secret
)

access_token = data["access_token"]

with open("access_token.txt", "w") as f:
    f.write(access_token)

print("\nAuthentication successful!")
print("Access token saved to access_token.txt")

kite.set_access_token(access_token)

profile = kite.profile()

print("\n===== USER PROFILE =====")
print(f"User ID: {profile['user_id']}")
print(f"Name: {profile['user_name']}")
print("Saved token:", access_token[:20])