import csv
import os


# Find directory of the current folder
path = os.path.realpath(__file__)
dir = os.path.dirname(path)

# Change directory to target folder
file_dir = dir.replace('uuv_mission', 'data')
os.chdir(file_dir)

# Store the CSV file in a list
with open('mission.csv', 'r') as file:
    read = csv.reader(file)
    data = list(read)

# print(data)