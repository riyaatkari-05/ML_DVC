import os
import csv

os.makedirs("data", exist_ok=True)

file_path = "data/data.csv"

with open(file_path, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([4, "David", 92])

print("New data added successfully.")
