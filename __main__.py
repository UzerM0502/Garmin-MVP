import argparse
from bronze_layer import BronzeLayer
from silver_layer import SilverLayer
from authenticate import authenticate_garmin
import datetime as dt
from db_models import DBModels

class Main:
    def __init__(self, garmin_username, garmin_password, start_date, end_date):
        self.garmin = authenticate_garmin(garmin_username, garmin_password)
        self.start_date = start_date
        self.end_date = end_date

    def run(self):
        # Bronze Layer
        bronze_layer = BronzeLayer(self.garmin, self.start_date, self.end_date)
        raw_df = bronze_layer.run()

        # Silver Layer
        silver_layer = SilverLayer(raw_df)
        silver_df = silver_layer.run()

        # Upload to SQLite
        db_models = DBModels(db_path='garmin_data.db')
        _ = db_models.upload_dataframe_to_sqlite('activities_data', silver_df)

        return silver_df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Garmin Data Pipeline")
    parser.add_argument("--username", required=True, help="Garmin username")
    parser.add_argument("--password", required=True, help="Garmin password")
    parser.add_argument("--start_date", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end_date", required=True, help="End date (YYYY-MM-DD)")
    args = parser.parse_args()

    garmin_username = args.username
    garmin_password = args.password
    start_date = dt.datetime.strptime(args.start_date, "%Y-%m-%d").date()
    end_date = dt.datetime.strptime(args.end_date, "%Y-%m-%d").date()

    main_process = Main(garmin_username, garmin_password, start_date, end_date)
    _ = main_process.run()
    print("Data processing completed successfully.")
    # print(silver_df.head())