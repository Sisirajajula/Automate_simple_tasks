import csv # library to read and write csv files
import secrets # to generate random passowrds for each user
import subprocess # This calls the useradd command, which creates and adds each user account.
from pathlib import Path #to locate data files for each user
cwd = Path.cwd() #current working directory
with open(cwd / "user_in.csv", "r") as file_input, open(cwd / "user_out.csv", "w") as file_output:
    reader = csv.DictReader(file_input) # reading the csv file as dictionary
    fieldnames = reader.fieldnames + ['password']
    writer = csv.DictWriter(file_output,fieldnames=fieldnames)
    writer.writeheader()
    for user in reader:
        user["password"] = secrets.token_hex(8)
        writer.writerow(user)