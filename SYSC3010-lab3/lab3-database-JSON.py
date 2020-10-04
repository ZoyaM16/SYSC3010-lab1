#!/usr/bin/env python3
import sqlite3
from urllib.request import * 
from urllib.parse import * 
import json

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa


# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
  # results is a JSON string
webData.close()

print (results)
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results

#current = data["main"]
#degreeSym = chr(176)

#print ("Temperature: %d%sF" % (current["temp"], degreeSym ))
#print ("Humidity: %d%%" % current["humidity"])
#print ("Pressure: %d" % current["pressure"] )

#current = data["wind"]
#print ("Wind : %d" % current["speed"])

#connect to database
dbconnect = sqlite3.connect("mydatabase2.db");
dbconnect.row_factory= sqlite3.Row;
#create a cursor to work with db
cursor = dbconnect.cursor();
#execute insert statemetn
cursor.execute('''create table if not exists windspeed(city test, windspeed Integer)''');

#create the columns 
cursor.execute('''insert into windspeed values (?,?)''',(city, data["wind"]["speed"]));

dbconnect.commit();
#execute select stmt
cursor.execute('SELECT * FROM windspeed');
#print
print("city \t windspeed")
for row in cursor:
    print((row['city']) + "\t" +str(row['windspeed']));
#close connection
dbconnect.close();

