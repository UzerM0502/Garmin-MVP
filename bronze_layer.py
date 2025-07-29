import pandas as pd
from datetime import datetime
from garminconnect import Garmin

class BronzeLayer:
    def __init__(self, garmin_client, start_date, end_date):
        self.garmin = garmin_client
        self.start_date = start_date
        self.end_date = end_date
        self.raw_df = pd.DataFrame()

    def run(self):
        activities = self._fetch_activities()
        if not activities:
            print("No activities fetched.")
            return pd.DataFrame()
        self.raw_df = self._to_dataframe(activities)
        return self.raw_df

    def _fetch_activities(self):
        try:
            activities = self.garmin.get_activities_by_date(
                self.start_date.isoformat(), self.end_date.isoformat()
            )
            print(f"[Bronze] Retrieved {len(activities)} activities.")
            return activities
        except Exception as e:
            print(f"[Bronze] Error fetching activities: {e}")
            return []

    def _to_dataframe(self, activities):
        df = pd.DataFrame(activities)
        print(f"[Bronze] Created DataFrame with shape: {df.shape}")
        return df
