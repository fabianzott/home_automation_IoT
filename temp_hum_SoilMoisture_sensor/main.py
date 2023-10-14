from machine import Pin, I2C
from time import sleep
import bme280
from umqtt.robust import MQTTClient
import machine

def init_bme280():
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    return bme280.BME280(i2c=i2c)

def init_mqtt():
    server = "<IP_address>"
    client_id = "temp_test"
    client = MQTTClient(client_id, server, port=1883)
    client.connect()
    return client

def read_sensor(bme):
    try:
        temp, pres, hum = bme.values
        temp = float(temp[:-1])
        hum = float(hum[:-1])
        return temp, hum
    except OSError:
        print("Failed to read sensor")
        return None, None

def main():
    bme = init_bme280()
    client = init_mqtt()

    while True:
        temp, hum = read_sensor(bme)
        
        if temp is not None and hum is not None:
            msg_hum = f"{hum}%"
            client.publish(b'humidity/esp2866/', msg_hum)
        else:
            print("Invalid sensor readings")

        sleep(5)

if __name__ == "__main__":
    main()
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
