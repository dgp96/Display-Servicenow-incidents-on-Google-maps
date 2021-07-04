#!/usr/bin/python
# -*- coding: utf-8 -*-
# Need to install requests package for python
# easy_install requests
#Pull incident data from servicenow and store them in 'servicenow.sqlite' database
import sqlite3
import requests
import json

conn = sqlite3.connect('servicenow.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Incident;

CREATE TABLE Incident (
    Sys_ID TEXT NOT NULL PRIMARY KEY UNIQUE,
    Number TEXT UNIQUE,
    Short_Description TEXT,
    Caller TEXT,
    Priority TEXT,
    Category TEXT,
    CMDB_CI TEXT,
    Location TEXT
);


''')

# Set the request parameters

url = \
    'https://dev92497.service-now.com/api/now/table/incident?sysparm_query=active%3Dtrue&sysparm_display_value=true&sysparm_fields=number%2Cshort_description%2Ccaller_id%2Cpriority%2Ccategory%2Ccmdb_ci%2Clocation%2Csys_id'

# Eg. User name="admin", Password="admin" for this code sample.

user = 'admin2'
pwd = 'admin'

# Set proper headers

headers = {'Content-Type': 'application/json',
           'Accept': 'application/json'}

# Do the HTTP request

response = requests.get(url, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 200

if response.status_code != 200:
    print (
        'Status:',
        response.status_code,
        'Headers:',
        response.headers,
        'Error Response:',
        response.json(),
        )
    exit()

# Decode the JSON response into a dictionary and use the data

data = json.dumps(response.json())
data = json.loads(data)

for entry in data['result']:
    sys_id = str(entry['sys_id'])
    number = str(entry['number'])
    short_description = str(entry['short_description'])
    if(len(entry['caller_id']) == 2):
        caller_id = str(entry['caller_id']['display_value'])
    else:
        caller_id = ''
    priority = str(entry['priority'])
    category = str(entry['category'])
    cmdb_ci = str(entry['cmdb_ci'])
    if(len(entry['cmdb_ci']) == 2):
        cmdb_ci = str(entry['cmdb_ci']['display_value'])
    else:
        cmdb_ci = ''
    location = str(entry['location'])
    if(len(entry['location']) == 2):
        location = str(entry['location']['display_value'])
    else:
        location = ''


    print (
        sys_id,
        number,
        short_description,
        caller_id,
        priority,
        category,
        cmdb_ci,
        location
        )

    if sys_id is None or number is None:
        print ('Skipping this record as sys_id or number is absent')
        continue

    cur.execute('''INSERT OR IGNORE INTO Incident (Sys_ID, Number, Short_Description, Caller, Priority, Category, CMDB_CI, Location)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)'''
                , (
        sys_id,
        number,
        short_description,
        caller_id,
        priority,
        category,
        cmdb_ci,
        location
        ))

    conn.commit()
