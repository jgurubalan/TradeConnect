from kite_session import kite


profile = kite.profile()

print("=" * 45)
print("              KITE PROFILE")
print("=" * 45)

print()
print(f"User ID        : {profile['user_id']}")
print(f"User Type      : {profile['user_type']}")
print(f"Name           : {profile['user_name']}")
print(f"Short Name     : {profile['user_shortname']}")
print(f"Email          : {profile['email']}")
print(f"Broker         : {profile['broker']}")

print()
print("-" * 45)
print("ACCOUNT ACCESS")
print("-" * 45)

print(f"Exchanges      : {', '.join(profile['exchanges'])}")
print(f"Products       : {', '.join(profile['products'])}")
print(f"Order Types    : {', '.join(profile['order_types'])}")

print()
print("-" * 45)
print("META")
print("-" * 45)

for key, value in profile["meta"].items():
    print(f"{key:<15}: {value}")

print()
print("-" * 45)
print("AVATAR")
print("-" * 45)

print(profile["avatar_url"])

print()
print("=" * 45)
print("Logging out...")
print("=" * 45)

kite.invalidate_access_token()

print("Session closed")
print("=" * 45)