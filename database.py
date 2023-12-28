import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

db_connection_string = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4" 
# db_connection_string = os.environ['DATABASE_URL']

engine = create_engine(db_connection_string, connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        columns = result.keys()
        jobs = []
        for row in result:
            jobs_dict = {}
            for column, value in zip(columns, row):
                jobs_dict[column] = value
            jobs.append(jobs_dict)
        return jobs

def load_job_from_db(job_id):
    with engine.connect() as conn:
        # Execute the query with the provided job ID
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"), {'val': job_id}
        )
        # Retrieve the column names from the result
        columns = result.keys()
        # Initialize a variable to hold the job data
        job_dict = None
        for row in result:
            job_dict = {}
            for index, column in enumerate(columns):
                job_dict[column] = row[index]
            break
        return job_dict


