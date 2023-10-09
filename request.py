import json
from auth import headers
import requests

class Request:
    def __init__(self):
        self._headers = headers
    @staticmethod
    def get_content(url: str, param: dict) -> str:
        try:
            reponse = requests.get(url=url, params=param, headers=headers)
            reponse.raise_for_status()
            if reponse.status_code == 200:
                return reponse.json()
        except requests.exceptions.RequestException as e:
            return None

