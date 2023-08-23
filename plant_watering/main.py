from time import time, sleep, 
import time
import ntptime  # NPT server for accurate time with utime module
import utime
import machine
from stepperTEST import STEPPER
try:
    import usocket as socket
except:
    import socket
from umqtt.simple import MQTTClient
import ubinascii
import micropython
import network
import esp32
import esp
esp.osdebug(None)
import gc
gc.collect()
import ntptime

############# Connect to WiFi Network ###########

ssid = 'FRITZ!Box 7530 PX'
password = '49920537718620591561'


def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('FRITZ!Box 7530 PX', '49920537718620591561')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_connect()

######### MQTT Topics ####################

SERVER = '192.168.178.52'  # MQTT Server Address
CLIENT_ID = 'temp_test'
TOPIC_stepper = b'stepper/#'
TOPIC_stepper_state = b'stepper/run/'
client = MQTTClient(CLIENT_ID, SERVER, port=1883)
client.connect()


# def restart_and_reconnect():
#     print('Failed to connect to MQTT broker. Reconnecting...')
#     time.sleep(10)
#     machine.reset()

# try:
#     client = connect_and_subscribe()
# except OSError as e:
#     restart_and_reconnect()

######### Stepper #########################

motor_config = {
    'In1': 32,
    'In2': 33,
    'In3': 26,
    'In4': 25,
    'number_of_steps': 200,
    'max_speed': 80
}

stepper = STEPPER(motor_config)

############ Get current time ################

# Get the current local time before synchronization
previous_time = utime.localtime()

# Connect to an NTP server and synchronize the time
ntptime.settime()

UTC_OFFSET = 2 * 60 * 60  # change the '2' according to your timezone
current_time_berlin = time.localtime(time.time() + UTC_OFFSET)

# Get the current local time after synchronization
# current_time = utime.localtime()

# Compare the time before and after synchronization
if previous_time != current_time_berlin:
    print("Time synchronization successful.")
else:
    print("Time synchronization failed.")

# Extract individual time components
year = current_time_berlin[0]
month = current_time_berlin[1]
day = current_time_berlin[2]
hour = current_time_berlin[3]
minute = current_time_berlin[4]
second = current_time_berlin[5]

# Print the current local time
print("Current Time: {}-{}-{} {}:{}:{}".format(year, month, day, hour, minute, second))

######### Infinite Loop ####################

while True:
    try:
        ####### Timer to start pump evening ##############
        time_to_pump_1 = (0, 0, 0, 21, 0, 30, 0, 0)
        time_to_pump_2 = (0, 0, 0, 21, 15, 30, 0, 0)
        time_to_pump_3 = (0, 0, 0, 21, 30, 30, 0, 0)
        ####### Timer to start pump morning ##############
        time_to_pump_4 = (0, 0, 0, 7, 0, 30, 0, 0)
        time_to_pump_5= (0, 0, 0, 7, 15, 30, 0, 0)
        time_to_pump_6 = (0, 0, 0, 7, 45, 30, 0, 0)
        # Get the current local time
        current_time = utime.localtime()
        current_time = time.localtime(time.time() + UTC_OFFSET)  # adjust to Berlin time +2h
        # Set seconds and milliseconds to zero
        current_time = list(current_time)
        current_time[0] = 0  # Set year to zero
        current_time[1] = 0  # Set month to zero
        current_time[2] = 0  # Set days to zero
        # current_time[5] = 0  # Set seconds to zero
        current_time[6] = 0  # Set milliseconds to zero
        current_time[7] = 0  # Set microseconds to zero
        current_time = tuple(current_time)
        print(current_time)
        #client.publish(TOPIC_stepper_state, msg_time_stamp)
        if time_to_pump_1 == current_time or time_to_pump_2 == current_time or time_to_pump_3 == current_time or time_to_pump_4 == current_time or time_to_pump_5 == current_time or time_to_pump_6 == current_time:
            print('Motor initiate motor!')
            rotation = 360 * 200
            speed = 80
            stepper.step(rotation, speed)
            stepper.release()
            ###### Publishing local time with status #########
            year, month, day, hour, minute, second, _, _ = current_time
            msg_time_stamp = str(year) + "/" + str(month) + "/" + str(day) + "/" + str(hour) + "/" + str(
            minute) + "/" + str(second)
            client.publish(TOPIC_stepper_state, msg_time_stamp)
            print('Motor was activated')          
        time.sleep(1)
    except Exception as e:
        print("An error occurred:", e)
        machine.reset()

