import os
import requests
from dotenv import load_dotenv

load_dotenv()


class HDFCConnect:

    def __init__(self):
        self.api_key = os.getenv("HDFC_API_KEY")
        self.api_secret = os.getenv("HDFC_API_SECRET")
        self.token = None

    def login(self):

        url = "https://developer.hdfcsec.com/oapi/v1/login"

        payload = {
            "api_key": self.api_key,
            "api_secret": self.api_secret
        }

        response = requests.post(
            url,
            json=payload
        )

        data = response.json()

        print(data)

        self.token = data.get("access_token")

        return self.token


    def headers(self):

        return {
            "Authorization": self.token,
            "api_key": self.api_key
        }


    def profile(self):

        url = "https://developer.hdfcsec.com/oapi/v1/profile"

        r = requests.get(
            url,
            headers=self.headers()
        )

        return r.json()