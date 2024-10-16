import csv
import os


# Change directory to the folder with the data in
file_path = "\data"
os.chdir(os.getcwd() + file_path)

# Store the CSV file in a list
with open('mission.csv', 'r') as file:
    read = csv.reader(file)
    data = list(read)

# print(data)