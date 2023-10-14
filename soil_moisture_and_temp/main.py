from machine import Pin, I2C, ADC
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

def read_bme280(bme):
    temp, pres, hum = bme.values
    return float(temp[:-1]), float(pres[:-3]), float(hum[:-1])

def read_moisture(adc, min_val, max_val):
    moist = adc.read_u16()
    return convert_to_percent(moist, min_val, max_val, 100, 0)

def convert_to_percent(x, in_min, in_max, out_min, out_max):
    return round((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def main():
    bme = init_bme280()
    client = init_mqtt()
    adc = ADC(0)
    min_val, max_val = 11519, 38143

    while True:
        temp, pres, hum = read_bme280(bme)
        moist_percent = read_moisture(adc, min_val, max_val)
        
        if all(isinstance(val, (float, int)) for val in [temp, hum, pres, moist_percent]):
            client.publish(b'humidity/esp2866/', f"{hum}")
            sleep(0.1)
            client.publish(b'temperature/esp2866/', f"{temp}")
            sleep(0.1)
            client.publish(b'pressure/esp2866/', f"{pres}")
            sleep(0.1)
            client.publish(b'moisture/esp2866/', f"{moist_percent}")
            sleep(0.1)
        else:
            print("Invalid sensor readings")

        sleep(10)

if __name__ == "__main__":
    main()
