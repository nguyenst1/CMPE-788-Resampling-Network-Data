import os
import glob
import pandas as pd
import csv


labels = []

# Open the CSV feature file for reading
with open('data/UNSW-NB15 - CSV Files/NUSW-NB15_features.csv', 'r') as csvfile:
    # Create a reader object to read in the CSV file
    csvreader = csv.reader(csvfile)

    # Loop through each row in the CSV file
    for i, row in enumerate(csvreader):
        if i == 0:
            continue

        # Process the row here
        labels.append(row[1].lower())



csv_dir = 'data/UNSW-NB15 - CSV Files/main_csv_samples'
data = [labels]

# Get a list of all CSV files in the directory
csv_files = glob.glob(os.path.join(csv_dir, "*.csv"))

# Loop over each CSV file
for file in csv_files:
    # Open the CSV file for reading
    with open(file, "r", newline="") as infile:
        reader = csv.reader(infile) # Initialize a CSV reader object
        for row in reader: # Loop over each row in the CSV file and append it to the data list
            assert(len(labels) == len(row))
            data.append(row)


# Open a new CSV file for writing
with open("concat.csv", "w", newline="") as outfile:

    # Initialize a CSV writer object
    writer = csv.writer(outfile)

    # Write each row in the data list to the output CSV file
    for row in data:
        writer.writerow(row)

print("Concatenated and converted CSV file created!")