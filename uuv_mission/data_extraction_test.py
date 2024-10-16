import csv
import os
import pandas as pd
import numpy as np


# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())

# Change directory to the folder with the data in
file_path = "\data"
os.chdir(os.getcwd() + file_path)

# Store the CSV file using pandas
df = pd.read_csv('mission.csv')
data = df.values

# Store the CSV file in a list
# with open('mission.csv', 'r') as file:
#     read = csv.reader(file)
#     data = np.array(read)

# print(data)
# print(data[:, 0])