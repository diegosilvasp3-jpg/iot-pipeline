import os
from sqlalchemy import create_engine
import pandas as pd

HOST = os.getenv("POSTGRES_HOST", "localhost")
PORT = os.getenv("POSTGRES_PORT", 5432)
USER = os.getenv("POSTGRES_USER", "postgres")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DB = os.getenv("POSTGRES_DB", "iot")

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}")

def main():
    print("Lendo data\\temperature_readings.csv...")
    df = pd.read_csv("data/temperature_readings.csv")
    print("Gravando no PostgreSQL...")
    df.to_sql("temperature_readings", con=engine, if_exists="replace", index=False)
    print("Concluído!")

if __name__ == "__main__":
    main()
