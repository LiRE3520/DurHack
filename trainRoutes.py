import requests
import json
from requests.auth import HTTPBasicAuth
import csv

API_USERNAME = 'rttapi_tobyp'
API_KEY = '241eeb90b4edcfe9be6bc3adf00e78b7f898f13d'
BASE_URL = 'https://api.rtt.io/api/v1/json/search/'

def to_crs(item, column_name='Description'):
    with open('./static/stations/cif_tiplocs.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)

        # Check if the specified column exists in the CSV file
        if column_name not in reader.fieldnames:
            print(f"Column '{column_name}' not found in the CSV file.")
            return False

        # Iterate through the rows to check for the item in the specified column
        for row in reader:
            if row[column_name] == item.upper():
                # return the crs code
                print(f'found: {row["CRS"]}')
                return row['CRS']
    print(f"Item '{item}' not found in the CSV file.")
    return False

def fetch_train_times(origin):
    response = requests.get(f"https://api.rtt.io/api/v1/json/search/{origin}", auth=HTTPBasicAuth(API_USERNAME, API_KEY))
    if response.status_code == 200:
        data = response.json()
        print(f"printing data: {data}")
        timesList = []
        try:
            for service in data['services']:
                timesList.append([service['locationDetail']['origin'][0]['description'], service['locationDetail']['origin'][0]['publicTime'], service['locationDetail']['destination'][0]['description'], service['locationDetail']['destination'][0]['publicTime']])
            return timesList
        except:
            print('Error: ran out of services')
    else:
        print(f'Error: {response.status_code}')
        return None
    
origin = to_crs('cambridge')  # Station code for Manchester Piccadilly
destination = 'EUS'  # Station code for London Euston
time = '12:00'  # Departure time (24-hour clock)

#train_times = fetch_train_times(origin)
#print(train_times)
