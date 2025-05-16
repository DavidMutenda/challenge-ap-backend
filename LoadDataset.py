import json
import psycopg2

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


import json
import csv

# Load JSON data
with open('mock_student_data.json', 'r') as json_file:
    data = json.load(json_file)

# Open CSV file for writing
with open('data.csv', 'w', newline='') as csv_file:
    # Get keys from the first dictionary for header
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)





# Load and insert JSON data
with open('mock_student_data.json') as f:
    data = json.load(f)
    for entry in data:
        cur.execute("""
        INSERT INTO Students (id, first_name, last_name,email,gender,student_id,study_programme, secondary_school,registration_date,academic_year) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,)
        ON CONFLICT (id) DO NOTHING
        """, (entry['id'], entry['first_name'], entry['last_name'], entry['email'], entry['gender'], entry['student_id'], entry['study_programme'], entry['secondary_school'], entry['registration_date'], entry['academic_year']))

# Commit and close
conn.commit()
cur.close()
conn.close()
