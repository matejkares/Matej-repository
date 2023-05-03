import os
import requests
import zipfile

url = "https://vdp.cuzk.cz/vymenny_format/csv/20230430_OB_581291_ADR.csv.zip"
filename = "20230430_OB_581291_ADR.csv.zip"
folder = "C:\\Python\\ukol3"

if not os.path.exists(folder):
    os.makedirs(folder)

response = requests.get(url)
filepath = os.path.join(folder, filename)

with open(filepath, "wb") as file:
    file.write(response.content)
    
with zipfile.ZipFile(filepath, 'r') as zip_ref:
    zip_ref.extractall(folder)


import csv

csv_file_path = os.path.join(folder, "20230430_OB_581291_ADR.csv")
header = []

with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)


import pandas as pd

filename = "C:\\Python\\ukol3\\20230430_OB_581291_ADR.csv"
df = pd.read_csv(filename, sep=";", header=0, encoding="ANSI")


# Select rows where "Název ulice" is equal to "Ronovská"
df = df[df["Název ulice"] == "Ronovská"]

# Convert "Číslo orientační" to integer
df["Číslo orientační"] = df["Číslo orientační"].astype("Int64")

# Select only specific columns and display the resulting dataframe
selected_columns = ["Název ulice", "Číslo domovní", "Číslo orientační", "PSČ", "Název obce"]
df = df[selected_columns]

print(df)

# Write the resulting dataframe to a new CSV file
output_file_path = os.path.join(folder, "postovniadresy.csv")
df.to_csv(output_file_path, sep=";", index=False, encoding="ANSI")

print(f"Resulting dataframe:\n{df}")
print(f"\nThe resulting CSV file has been saved to {output_file_path}.")







