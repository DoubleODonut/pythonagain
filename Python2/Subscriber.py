from mosquitto import *
from serial import *
from random import *


SPEED = 9600
# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino

board = Serial("/dev/cu.usbmodem14411",SPEED,timeout=2)
randomID = random()
client = Mosquitto("Ged")
client.connect("10.212.61.136")
client.subscribe("/lights")
print("connected")

def messageReceived(broker, obj, msg):
    global client
    payload = msg.payload.decode()
    board.write(payload.encode()+'\n')
    print("Message " + msg.topic + " containing: " + payload)
        
	    #client = None
        
client.on_message = messageReceived
while (client != None): client.loop()



# The rest of your code goes in here !!!