import requests
import csv
import pandas as pd

def fetchData():
    URL = "https://random-data-api.com/api/v2/users"
    response = requests.get(URL)
    responseData = response.json()

    hey = [responseData["address"]["city"],responseData["address"]["street_name"],responseData["address"]["street_address"]]
    address = ','.join(hey)
    filteredData = {
        "id": responseData["id"],
        "first_name": responseData["first_name"],
        "last_name": responseData["last_name"],
        "username": responseData["username"],
        "email": responseData["email"],
        "avatar": responseData["avatar"],
        "gender": responseData["gender"],
        "date_of_birth": responseData["date_of_birth"],
        "address": address
    }
    data = []
    for key in filteredData:
        data.append(filteredData[key])

    return data

def addRandomEntries():
    users_csv_file = "users.csv"
    entries = int(input("Enter number of entries to add : "))

    with open(users_csv_file, 'a',newline='\n') as file:
        writer = csv.writer(file,delimiter=',')
        try:
            pd.read_csv(users_csv_file)
        except:
            writer.writerow(['id','first_name','last_name','username','email','avatar','gender','date_of_birth','address'])

        for x in range(entries):
            writer.writerow(fetchData())
            print("entry",x+1,"entered from try")
        
def sortData():

    usersData = []
    with open("users.csv", mode='r') as file:
        reader = csv.reader(file)
        for x in reader:
            usersData.append(x)
    usersData.pop(0)
    usersData.sort(key = lambda x: x[3])

    with open("users-sorted.csv", mode='w', newline='\n') as file:
        writer = csv.writer(file,delimiter=',')
        usersData.insert(0,['id','first_name','last_name','username','email','avatar','gender','date_of_birth','address'])
        writer.writerows(usersData)

def findUser():
    yourData = input("Enter your Id or username : ")
    try:
        with open("users.csv", 'r') as file:
            reader = csv.reader(file)
            for x in reader:
                if(x[0] == yourData):
                    print("ID :",x[0],"\nFirst name :",x[1],"\nLast name :",x[2],"\nUsername :",x[3],"\nEmail :",x[4],"\nAvatar :",x[5],"\nGender :",x[6],"\nDOB :",x[7],"\nAddress :",x[8])
    except:
        print("File isn't available for finding the user")