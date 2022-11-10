import requests
import csv
import pandas as pd

URL = "https://random-data-api.com/api/v2/users"
response = requests.get(URL)
data = response.json()
filteredData = {
    "id": data["id"],
    "first_name": data["first_name"],
    "last_name": data["last_name"],
    "username": data["username"],
    "email": data["email"],
    "avatar": data["avatar"],
    "gender": data["gender"],
    "date_of_birth": data["date_of_birth"],
    "address": data["address"]
}

users_csv_headers = ['id','first_name','last_name','username','email','avatar','gender','date_of_birth','address',]
users_csv_file = "users.csv"

try:
    with open(users_csv_file, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=users_csv_headers)
        writer.writerow(filteredData)
except:
    print("err")

df = pd.read_csv("users.csv")
print(df)