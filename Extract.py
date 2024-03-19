import os
import google_auth_oauthlib
from googleapiclient.discovery import build
from IPython.display import JSON
import pandas as pd

api_key = 'AIzaSyBAmW8JoXmNvKtjADGK_OuvuMc0UJtOa7g'


api_service_name = "youtube"
api_version = "v3"

def Youtube():
    # Get credentials and create an API client
    youtube = build(
    api_service_name, api_version, developerKey=api_key)
    return youtube