# Complete project details at https://RandomNerdTutorials.com
import socket
###### BME280 #########
from machine import Pin, I2C
from machine import ADC
from time import sleep
import bme280
from umqtt.robust import MQTTClient # here umqtt.robust package is used

######### Soil Moisture #####
adc = ADC(0)
max_val = 38143   # this value has to be observed and can change over time -> absolute calibration is too time consuming
min_val = 11519   # this value has to be observed and can change over time -> absolute calibration is too time consuming

def convert_to_percent(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# ESP8266 - Pin assignment
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)


SERVER = '<IP_adress>'  # local MQTT Server Address -> Raspberry Pi
CLIENT_ID = 'temp_test'
TOPIC_temp = b'temperature/esp2866/'
TOPIC_pres = b'pressure/esp2866/'
TOPIC_hum = b'humidity/esp2866/'
TOPIC_moist = b'moisture/esp2866/'

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
      
      ########### Soil Moisture #########
      moist = adc.read_u16()
      moist = int(moist)
      moist_percent =  convert_to_percent(moist, min_val, max_val, 100, 0) # sometimes neg -> dynamic calibration
      moist_percent = round(moist_percent)
      print(moist_percent)
        
      ################ MQTT #############     
      if isinstance(temp, float) and isinstance(hum, float) and isinstance(pres, float) and isinstance(moist_percent, int):
          msg_temp = str(temp)# + "°C"
          msg_hum = str(hum)# + "%"
          msg_pres = str(pres)
          msg_moist = str(moist_percent)
          #msg = (b'{0:3.2f}, {0:3.2f}'.format(temp, hum))
          #.publish(TOPIC_temp, msg_temp)
          client.publish(TOPIC_hum, msg_hum)
          time.sleep_ms(100)
          client.publish(TOPIC_temp, msg_temp)
          time.sleep_ms(100)
          client.publish(TOPIC_pres, msg_pres)
          time.sleep_ms(100)
          client.publish(TOPIC_moist, msg_moist)
          time.sleep_ms(100)
          #print(msg_temp, msg_hum)
      else:
          print('Invalid sensor readings')
    except OSError:
        print('Failed to read sensor')

    sleep(10)
