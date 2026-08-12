from hdfc import HDFCConnect


hdfc = HDFCConnect()

token = hdfc.login()

print("TOKEN:")
print(token)


print("PROFILE:")
print(
    hdfc.profile()
)