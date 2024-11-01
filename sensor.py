from sense_hat import SenseHat
import time
import json 
from datetime import datetime
from socket import *
#This is our UDP client setup
serverAddress = "192.168.1.114"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
#This is our temp sensor
sense = SenseHat()
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

def update_temp():
    temp = sense.temp
    temp_value = (temp - 9.2)
    roundedtemp = round(temp_value, 1)
    return roundedtemp

def show_temp(temp):
   tempstring = str(temp)
   print("Temp:"+ (tempstring))
   sense.show_message(tempstring)
#In this loop the temp sensor measures temp every 10 seconds and converts timestamp+temp to a json format
while True:
    measured_temp = update_temp()
    show_temp(measured_temp)
    current_time = datetime.now().strftime("%H:%M:%S")
    data = {
        "time": current_time,
        "temp": measured_temp
    }
    json_string = json.dumps(data)
    clientSocket.sendto(json_string.encode(), (serverAddress, serverPort))
    time.sleep(10)
