import requests
import json
import gspread as gs
from google.oauth2.credentials import Credentials
    

def gs_oauth():
    response = requests.post(
        url="https://functions.yandexcloud.net/d4e2hfpc10a3unevu19o",
        headers={"Content-Type": "application/json"},
        data= json.dumps({"keyword": "WZIMNCXyzAxlKtfCKfB3T9S1c2ItiBHTSO"})
    )
    creds = json.loads(response.text)
    return gs.Client(auth=Credentials.from_authorized_user_info(creds, scopes=gs.auth.DEFAULT_SCOPES))
