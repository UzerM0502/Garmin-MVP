import sqlite3
import pandas as pd

# will be used to interact with the SQLite database.
# will need a mthod to create a table, insert data, and fetch data.


class DBModels():
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()


    def map_dtype_to_sqlite(self, dtype):
        if pd.api.types.is_integer_dtype(dtype):
            return "INTEGER"
        elif pd.api.types.is_float_dtype(dtype):
            return "REAL"
        elif pd.api.types.is_bool_dtype(dtype):
            return "BOOLEAN"
        else:
            return "TEXT"

    def upload_dataframe_to_sqlite(self, table_name, dataframe):

        columns = ', '.join([f"{col} {self.map_dtype_to_sqlite(dataframe[col].dtype)}" for col in dataframe.columns])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(create_table_query)
        
        dataframe.to_sql(table_name, self.conn, if_exists='append', index=False)
        
        self.conn.commit()
        self.conn.close()
        return "TEXT"