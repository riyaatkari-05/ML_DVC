import os
import csv
os.makedirs("data", exist_ok=True)

file_path = "data/data.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Score"])
    writer.writerow([1, "Alice", 85])
    writer.writerow([2, "Bob", 90])
    writer.writerow([3, "Charlie", 78])

print("Data created successfully.")
