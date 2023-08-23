# home_automation_IoT
Collection of some of my home automation projects using MQTT protocol and HiveMQ IoT Server

My goal was to have an active IoT data conncetion between my phone and my self-made smart home sensors and projects.

Details about the setup:
- since I have no public IP addess I use a free HiveMQ MQTT cloud server (https://www.hivemq.com/mqtt-cloud-broker/)
- Mosquitto is running on my local Raspberry Pi functioning as a local broker (Mosquitto MQTT Bridge to HiveMQ server)
- the "IoT MQTT Panel pro" app on Android is used for data vizualisation and communication (both publish and subscribe possible, https://play.google.com/store/apps/details?id=snr.lab.iotmqttpanel.prod&pcampaignid=web_share)
- Sensors connected to either an ESP32 or ESP2866 with MicroPython using umqtt.simple package for communication

Communnication scheme:
Sensors/relais <-> ESP32/2866 <-> Rapsberry Pi (Mosquitto bridge in local network) <-> HiveMQ cloud <-> Android smart phone 
