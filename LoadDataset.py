import json
import psycopg2
import pandas as pd

# Step 1: Load CSV with pandas
csv_file_path = 'mock_student_data.csv'
df = pd.read_csv(csv_file_path)


# PostgreSQL connection details
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="80235"
)
cur = conn.cursor()

# Create table (adjust columns as needed)
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    gender TEXT,
    student_id UUID,
    study_programme TEXT,
    secondary_school TEXT,
    registration_date DATE,
    academic_year INTEGER

)
""")


# Step 4: Insert data using `execute_values` for performance
from psycopg2.extras import execute_values

# Convert DataFrame to list of tuples
data_tuples = list(df.itertuples(index=False, name=None))

# Build insert query
columns = ','.join(df.columns)
insert_query = f"INSERT INTO students ({columns}) VALUES %s"

execute_values(cur, insert_query, data_tuples)
#Commit all.
# Commit and close
conn.commit()
cur.close()
conn.close()
