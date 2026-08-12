from kite_session import kite

try:
    profile = kite.profile()
    print("PROFILE OK")
    print(profile["user_id"])
except Exception as e:
    print("PROFILE FAILED")
    print(type(e).__name__, e)

try:
    margins = kite.margins()
    print("MARGINS OK")
    print(margins)
except Exception as e:
    print("MARGINS FAILED")
    print(type(e).__name__, e)