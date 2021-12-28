from time import sleep
import firebase_admin
from firebase_admin import credentials, storage, db
import os
from sense_hat import SenseHat
import datetime
from dotenv import dotenv_values

# Create SenseHAT object (used to access temp sensor when creating message)
sense = SenseHat()
temperature=round(sense.temperature,2)
humidity=round(sense.humidity)
pressure=round(sense.pressure)
currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

#load configuration values from .env file
config = dotenv_values(".env")

#Configuration parameters
deviceID = config["deviceID"]
interval = int(config["transmissionInterval"])

cred=credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'sensepi-d6fe8.appspot.com',
    'databaseURL': 'https://sensepi-d6fe8-default-rtdb.firebaseio.com/'    
})

bucket = storage.bucket()

ref = db.reference('/')
home_ref = ref.child('file')

def store_file(fileLoc):

    filename=os.path.basename(fileLoc)

    # Store File in FB Bucket
    blob = bucket.blob(filename)
    outfile=fileLoc
    blob.upload_from_filename(outfile)

def push_db(fileLoc, time):

  filename=os.path.basename(fileLoc)
  

  
if __name__ == "__main__":
    f = open("./test.txt", "w")
    f.write("a demo upload file to test Firebase Storage")
    f.close()
    store_file('./test.txt')
    push_db('./test.txt', '12/11/2020 9:00' )

 # Push file reference to image in Realtime DB

while True:
 home_ref.push({     
    'Temperature': temperature,
    'Humidity': humidity,
    'Pressure': pressure,
    'Device': deviceID,
    'timestamp': currentTime}    
 )
 sleep(interval)