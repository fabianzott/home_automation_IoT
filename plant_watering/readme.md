A short guide to safe my tomatoe plants during vacation. 
If you have no time or no coding experience, do the [quick-fix](https://www.blumat.de/blumat-classic).

My setup:

- ESP32 microcontroller
- L298N stepper motor driver
- NEMA17 dosing pump

The plants are watered in the morning and in the evening at predefined times (see main.py). The L298N stepper motor driver can get !!!very hot!!! so I pump water three times with a cool down period of 15min in between. The systems sends status messages via MQTT IoT protocoll when the pump is activated.
Remote activation via my app was too unstable.
