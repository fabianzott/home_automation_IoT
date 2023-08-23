import socket
###### BME280 #########
from machine import Pin, I2C
from time import sleep
import bme280
from umqtt.robust import MQTTClient 


# ESP8266 - Pin assignment
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)


SERVER = '<IP_adress>'  # local MQTT Server Address -> Raspberry Pi
CLIENT_ID = 'temp_test'
TOPIC_temp = b'temperature/esp2866/'
TOPIC_pres = b'pressure/esp2866/'
TOPIC_hum = b'humidity/esp2866/'

client = MQTTClient(CLIENT_ID, SERVER, port=1883)
client.connect()



while True:
    try:
      ########## BME280 loop ###########
      sensor_data = bme.values  
      #print(bme.values)
      temp, pres, hum = sensor_data
      temp = float(temp[:-1])
      pres = float(pres[:-3])
      hum = float(hum[:-1])
      #print(temp)
      #print(pres)
      #print(hum)
        
      ################ MQTT #############     
      if isinstance(temp, float) and isinstance(hum, float):
          #msg_temp = str(temp) + "°C"
          msg_hum = str(hum) + "%" 
          #msg = (b'{0:3.2f}, {0:3.2f}'.format(temp, hum))
          #.publish(TOPIC_temp, msg_temp)
          client.publish(TOPIC_hum, msg_hum)
          
          #print(msg_temp, msg_hum)
      else:
          print('Invalid sensor readings')
    except OSError:
        print('Failed to read sensor')

    sleep(5)
