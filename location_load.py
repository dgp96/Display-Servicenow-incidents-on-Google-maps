import sqlite3
import json
import codecs
from geopy.geocoders import Nominatim
#Write incidents into the 'where.js' file in JSON format

geolocator = Nominatim(user_agent="myarsenal96@gmail.com")
conn = sqlite3.connect('servicenow.sqlite')
cur = conn.cursor()
#SELECT Location, group_concat(Number) FROM Incident GROUP BY Location
cur.execute('SELECT Location, group_concat(Number) as Incidents, count(*) as Count FROM Incident GROUP BY Location')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
location_incident_mapping = {}

for row in cur :

    data = str(row[0])
    if data is None : continue
    #if location_incident_mapping.get(data) is None : location_incident_mapping[data] = str(row[1])
    #else : location_incident_mapping[data] = location_incident_mapping[data] + ',' + str(row[1])
    incidents = str(row[1])
    incident_count = str(row[2])
    try:
        location = geolocator.geocode(data)
        lat = location.latitude
        lng = location.longitude
        if lat == 0 or lng == 0 : continue
        where = location.address
        where = where.replace("'", "")
    except:
        continue

    try :
        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+ "' , '"+ incidents + "', " + incident_count +"]"
        print(output)
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
print('Mapping ', location_incident_mapping)
