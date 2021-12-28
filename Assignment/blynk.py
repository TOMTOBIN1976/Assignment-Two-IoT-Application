import BlynkLib
from sense_hat import SenseHat
import time

BLYNK_AUTH = '1Als7JxqHf8R8ZcBNYYrTDwR5d81ERGK'

# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# register handler for virtual pin V1 write event
@blynk.on("V0")
def v3_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue=="1":
        sense.clear(255,255,255)
    else:
        sense.clear()

# infinite loop that waits for event

while True:
    blynk.run()
#   Adjust temperature reading following calibration 
    senseHatTemperature = sense.temperature
    calibratedTemperature = (senseHatTemperature - 12)
    blynk.virtual_write(1, round(calibratedTemperature,2))
    blynk.virtual_write(2, round(sense.humidity,2))
    blynk.virtual_write(3, round(sense.pressure,2))
    blynk.virtual_write(4, round(sense.rotation,2))
    blynk.virtual_write(5, (sense.gamma)) 
    blynk.virtual_write(6, round(sense.compass,2))
    blynk.virtual_write(7, round(calibratedTemperature,2))        
    time.sleep(1)