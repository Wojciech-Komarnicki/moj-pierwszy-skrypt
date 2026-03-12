import pandas as pd
from sqlalchemy import create_engine
from config import CONNECTION_STRING

class DatabaseManager:
    def __init__(self):
        self.engine = create_engine(CONNECTION_STRING)

    def save_to_db(self, df, table_name='sensor_readings'):
        try:
            df.to_sql(table_name, con=self.engine, index=False, if_exists='replace')
        except Exception as e:
            print(f"Error: {e}")

    def load_from_db(self, query):
        return pd.read_sql(query, con=self.engine)