# Fabian L. Zott 05/2022

########################
import socket
import machine
from machine import Pin
from time import time, sleep
from umqtt.robust import MQTTClient


###### define Relay pin(s)##########
relay = Pin(14, Pin.OUT) #  ESP8266 GPIO 14 (D5)
relay.value(1)           # (1) high signal for normally open relays -> off
relay_state = b"isoff"


###### MQTT topics ###########
relais_command = b'relais/command/'
relais_status = b'relais/status/'
relais_status_pub = b'relais/status/pub'

#relais_status_switch = b'relais/status/'
#relais_status_pub = b'relais/status/pub'


######### callback function ##########
def callback(topic, msg):
    global relay_state
    if topic == relais_command:
        print("Received in command callback:", msg)
        msg = msg.decode().lower()
        if msg.startswith('ison'):
            relay.value(0)
            relay_state = b"ison"
            #sleep(1)
            client.publish(topic=relais_status_pub, msg=relay_state, qos=1)         
        elif msg.startswith('isoff'):
            relay.value(1)
            relay_state = b"isoff"
            #sleep(1)
            client.publish(topic=relais_status_pub, msg=relay_state, qos=1)
    elif topic == relais_status:
        print("Received in status callback:", msg)
        msg = msg.decode().lower()
        if msg.startswith(b'ping'):
            client.publish(topic=relais_status_pub, msg=relay_state, qos=1)

######## connect to MQTT server #########
def init_client():
    global client
    SERVER = '<IP_adress>'  # local MQTT Server Address -> Raspberry Pi
    CLIENT_ID = 'temp_test'
    print("Trying to connect to mqtt broker.")    
    try:
        client = MQTTClient(CLIENT_ID, SERVER, port=1883)
        client.connect()
        client.set_callback(callback)
        print("Connected to MQTT client....")
        client.subscribe(relais_command, qos=2)  
        print("Subscribed to %s topic" % relais_command)
        client.subscribe(relais_status, qos=2)
        print("Subscribed to %s topic" % relais_status)
    except Exception as e:
        
        print("Could not connect to MQTT server.")
        sleep(10)
        print("Resetting machine in 10 sec.")
        machine.reset()

init_client()
clock = False

while True:
    try:
        client.check_msg()
  
