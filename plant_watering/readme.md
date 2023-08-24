A short guide to safe my tomatoe plants during vacation. 
If you have no time or no coding experience, do the [quick-fix](https://www.blumat.de/blumat-classic).

## My setup

- ESP32 microcontroller (install UMQTT.simple, etc. packages with Thonny)
- L298N stepper motor driver
- NEMA17 dosing pump

![scheme](https://github.com/fabianzott/home_automation_IoT/assets/85985274/92a8d620-06fe-4054-a97c-94909ba3a2c0)


## Watering Strategy
Your tomato plants will receive water twice a day – in the morning and evening. Refer to the main.py file for predefined watering times. However, an important note: the L298N stepper motor driver can become very hot during operation. To counteract this, the system pumps water three times with a cooling-off period of 15 minutes between each watering cycle.

## MQTT Status Messages
Stay informed about your plant's well-being even from afar. The system sends status messages, including timestamps, via the MQTT IoT protocol whenever the dosing pump is activated. This insight provides peace of mind that your plants are being tended to as planned.

## Issues
Remote activation via "MQTT IoT Broker" app was too unstable, e.g. sometimes blocking the channel.

## To do
In the future I will add a real time clock module.
