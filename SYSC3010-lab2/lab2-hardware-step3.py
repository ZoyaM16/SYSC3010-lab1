#description: This code continially dipalys the temperature, humidity and pressure of
#a room on the sense hat LED board. It was completed using the youtube tutorial at the beginning of lab2

from sense_hat import SenseHat #import vlaues from the sensehat to raspberry pi
import time #time helps me keep a log of all the vlues were measuring 
from time import asctime 

#assign the sense hat vlaues to a variable know as sense
sense = SenseHat()

#infinate while loop that will continually meaure the temp, humidity, and pressure

while True:
    temp=round(sense.get_temperature()*1.8 +32) #fxn get_temperature will give value measured by sense hat in degress celcuis whihc will be stored in temp variable 
    humidity = round(sense.get_humidity())
    pressure = round(sense.get_pressure())
    message = ' T=%dF. H=%d, P=%d ' %(temp,humidity,pressure) #store temp, pressure, and humidity with a specific notation in "message" string 
    sense.show_message(message, scroll_speed=(0.08), text_colour=[200,240,200], back_colour=[0, 0, 0]) #call in which i can send any message to my sense hat display screen. passing message string
    time.sleep(4) #this delays between each measuremetn 
    log = open('weather.txt', "a") # i made a log file where i will write the present time and the temperature 
    now = str(asctime())
    log.write(now+''+message+'\n')
    print(message) #we will see the reading on the console by using this. now we will see it on the console and sense hat
    log.close()
    time.sleep(5)
