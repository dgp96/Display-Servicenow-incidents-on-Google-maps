# Display-Servicenow-incidents-on-Google-maps

Developed a Python program to extract incident ticket data from Servicenow and show it's geodistribution on Maps.
The python scripts 'incident_sqlite_insertion.py' and 'location_load.py' is scheduled to run everyday.
(Click on Start Windows, search for Task Scheduler, and open it.)
Check the images to know about it.

incident_sqlite_insertion.py --> Extracts incident data from Servicenow via RestAPI and stores it in SQLite Database
location_load.py --> loads data from SQLite database into where.js file and stores it in JSON format
where.html --> Displays data from where.js on the Maps
