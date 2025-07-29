import json
import os
from datetime import datetime
from garminconnect import Garmin
import datetime as dt 

def authenticate_garmin(username, password):
    """Authenticate with Garmin Connect."""
    try:
        garmin = Garmin(username, password)
        garmin.login()
        
        print("Successfully logged in to Garmin Connect.")
        return garmin

    except Exception as e:
        print(f"An error occurred while initializing the API: {e}")