#!/usr/bin/python3
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from urllib.parse import urlparse
import sys
import time
import json

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# parse mqtt url for connection details
url_str = 'mqtt://broker.emqx.io:1883/tomtobin/home'
url = urlparse(url_str)
base_topic = url.path[1:]
auth=None
# Connect
if (url.username):
    auth = {'username':url.username, 'password':url.password}


def main():
    # Publish a message
    while True:
        temp=round(sense.get_temperature(),2)
        humidity=sense.get_humidity()

        #Create JSON strings
        temp_sensor=json.dumps({"temperature":temp, "timestamp":time.time()}) 
        humidity_sensor=json.dumps({"humidity":humidity, "timestamp":time.time()}) 

        #Create array of MQTT messages
        temp_msg={'topic': base_topic +"/temperature", 'payload':temp_sensor}
        hum_msg={'topic':base_topic +"/humidity", 'payload':humidity_sensor}
        msgs=[temp_msg,hum_msg]

        #Publish array of messages
        publish.multiple(msgs, hostname=url.hostname, port=url.port, auth=auth)
        print("published")
        time.sleep(15)

if __name__ == "__main__":
    main()