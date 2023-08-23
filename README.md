# home_automation_IoT
Welcome to the Home Automation IoT repository! Here, you'll find an assortment of my home automation projects, all designed to leverage the power of the MQTT protocol and the HiveMQ IoT Server.

## Project Objective
The primary aim of this collection is to establish a seamless IoT data connection between my smartphone and my custom-designed smart home sensors and projects. While I regret that I'm unable to provide a comprehensive step-by-step guide due to time constraints, I'm hopeful that the insights shared here will aid you in troubleshooting issues that may arise in your own projects.

## Setup Overview
Let's delve into the key components that make up this setup:

<ins>**HiveMQ MQTT Cloud Server:**</ins> As I lack a public IP address, I've opted to utilize the free HiveMQ MQTT cloud server. This enables remote connectivity and communication. Check it out: [HiveMQ MQTT Cloud Server](https://www.hivemq.com/mqtt-cloud-broker/).

<ins>**Local Mosquitto Broker:**</ins> To facilitate communication within my local network, a Mosquitto broker runs on my trusty Raspberry Pi. This broker acts as a bridge, connecting my local network to the HiveMQ server.

<ins>**IoT MQTT Panel Pro App:**</ins> Data visualization and communication are made possible through the "IoT MQTT Panel Pro" app, available for Android devices. This versatile app supports both publishing and subscribing. Explore it here: [IoT MQTT Panel Pro on Google Play](https://play.google.com/store/apps/details?id=snr.lab.iotmqttpanel.prod&hl=en_US).

<ins>**Sensor and Relay Setup:**</ins> My sensors and relays are connected to either ESP32 or ESP2866 microcontrollers, which are programmed using MicroPython. The umqtt.simple package is employed for communication, ensuring seamless data exchange.

## Communication Flow
The communication path for this setup is as follows:

Sensors/Relays ←→ ESP32/ESP2866 ←→ Raspberry Pi (Local Mosquitto Broker via Wlan) ←→ HiveMQ Cloud ←→ Android Smartphone

Feel free to explore the repository and adapt the principles shared here to your own projects. While this may not be a comprehensive guide, I'm optimistic that the information here will be instrumental in addressing challenges you encounter.

If you have any questions or suggestions, don't hesitate to reach out!

Happy tinkering and automating!
