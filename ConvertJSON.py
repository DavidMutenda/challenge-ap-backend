import csv
import json

# Load JSON data
with open('mock_student_data.json', 'r') as json_file:
    data = json.load(json_file)

# Open CSV file for writing
with open('mock_student_data.csv', 'w', newline='') as csv_file:
    # Get keys from the first dictionary for header
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)