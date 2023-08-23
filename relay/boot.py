try:
  import usocket as socket
except:
  import socket


from time import sleep

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = '<WIFI_name>'
password = '<WIFI_password>'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False: # stop when not connected to wifi
  pass

print('Connection successful')
print(station.ifconfig())
