import requests
import csv
import pandas as pd

URL = "https://random-data-api.com/api/v2/users"
response = requests.get(URL)
data = response.json()

hey = [data["address"]["city"],data["address"]["street_name"],data["address"]["street_address"]]
address = ','.join(hey)

with open('users.csv', 'a') as file:
    writer = csv.writer(file, delimiter = ',')
    # writer.writerow(["id", "FirstName", "LastName", "Username", "Email", "Avatar", "Gender", "DoB", "Address"])
    writer.writerow([data["id"], data["first_name"], data["last_name"], data["username"], data["email"], data["avatar"], data["gender"], data["date_of_birth"], address])

df = pd.read_csv("users.csv")
print(df)

    