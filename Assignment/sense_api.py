#!/usr/bin/python3

import socket # Use to get IP Address

from flask import Flask, request
from flask_cors import CORS
from sense_hat import SenseHat
from flask import Flask, request, render_template

sense = SenseHat()
deviceID="TOMRPI"
#clear sensehat and intialise light_state
sense.clear()

#create Flask app instance and apply CORS
app = Flask(__name__)
CORS(app)

#HTTP GET request with a /sensehat/environment path will execute function current_environment().

@app.route('/sensehat/environment',methods=['GET'])
def current_environment():
    temperature=round(sense.temperature,2)
    calibratedTemperature =round(sense.temperature - 12,2)
    humidity=round(sense.humidity,2)
    pressure=round(sense.pressure,2)    
    msg = {"deviceID": deviceID,"temp":calibratedTemperature,"humidity":humidity,"pressure":pressure}
    return str(msg)+"\n"

@app.route('/sensehat/light',methods=['GET'])
def light_get():
    #check top left pixel value(==0 - off, >0 - on) 
    print(sense.get_pixel(0, 0)) 
    if sense.get_pixel(0, 0)[0] == 0:
        return '{"state":"off"}'
    else:
           return '{"state":"on"}'

@app.route('/') 
def index():
      calibratedTemperature =round(sense.temperature - 12,2)
      celcius = round(calibratedTemperature, 2)
      fahrenheit = round(1.8 * celcius + 32, 2)
      humidity = round(sense.humidity, 2)
      pressure = round (sense.pressure, 2)
      ip = '192.168.1.68'      
      return render_template('status.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure,ip=ip)

#Run API on port 5000, set debug to True
app.run(host='0.0.0.0', port=5000, debug=True)
