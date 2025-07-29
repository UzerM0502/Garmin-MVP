import pandas as pd

class SilverLayer:
    def __init__(self, raw_df):
        self.raw_df = raw_df
        self.silver_df = pd.DataFrame()

    def run(self):
        self.silver_df = self._select_activities()
        return self.silver_df

    def _select_activities(self):
        columns = [
            'activityId', 'activityName', 'aerobicTrainingEffect', 'aerobicTrainingEffectMessage',
            'anaerobicTrainingEffect', 'averageHR', 'averageRunningCadenceInStepsPerMinute',
            'averageSpeed', 'beginTimestamp', 'bmrCalories', 'calories', 'distance',
            'elevationCorrected', 'endTimeGMT', 'hrTimeInZone_1', 'hrTimeInZone_2',
            'hrTimeInZone_3', 'hrTimeInZone_4', 'hrTimeInZone_5', 'maxHR', 'maxSpeed',
            'moderateIntensityMinutes', 'movingDuration', 'startTimeGMT', 'steps'
        ]
        missing_cols = [col for col in columns if col not in self.raw_df.columns]
        if missing_cols:
            print(f"[Silver] Warning: Missing columns: {missing_cols}")

        df = self.raw_df[[col for col in columns if col in self.raw_df.columns]].copy()
        print(f"[Silver] Created silver DataFrame with shape: {df.shape}")
        return df
