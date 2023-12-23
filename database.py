import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()

# DB_HOST = os.getenv("DB_HOST")
# DB_USERNAME = os.getenv("DB_USERNAME")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_NAME = os.getenv("DB_NAME")

db_connection_string = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4" 

engine = create_engine(db_connection_string, connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        
        columns = result.keys()
        jobs = [{column: value for column, value in zip(columns, row)} for row in result]
    return jobs