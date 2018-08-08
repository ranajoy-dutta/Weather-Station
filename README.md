# Weather-Station
> Using Onion Omega 2+ and DHT-11
<br/>
***
This is a Prototype model for IoT. This model is suitable for any IoT device that supports Python. The system can be integrated 
to send data from the device to the cloud using MQTT protocol, which is a lightweight protocol for machine to machine communication.
On the other end, the system can be integrated for receiving the data over cloud for further analysis.
<br/>
***
## How the system works :
    The sender.py file is flashed into any micro controller like Arduino/Raspberry/Onion.<br/>
    The sender.py file is responsible for sending/publishing the data/values/parameter as a payload to cloud/broker.<br/>
    This data can collection of data fetched from the sensors. Broker is responsible for forwarding the same to all the
    subscribed listeners. The receiver.py is one of the subscribed listener. Once the receiver receives this
    payload/data, it can manage this data as per its needs like for just storing into data or for further analysis and
    machine learning and many more purposes.

## FILE LIST :

...|- templates
...     >- index.html
...|- dbSetup.py
...|- README.txt
...|- mydb.db
...|- receiver.py
...|- sender.py

## Dependencies in receiving server :-
...python v3
...flask
...flask-mqtt
...flask-socketio
...eventlet

## Dependencies in Sending equipment :-
...python v3
...paho-mqtt

## Suitable Public Brokers for MQTT :-
1. Eclipse - iot.eclipse.org
2. Mosquitto - test.mosquitto.org
3. Hive - broker.hivemq.com

You can also create your own private Broker for MQTT by using the software provided by hive at https://www.hivemq.com/downloads/


The project is still under its initial stages of development and we welcome any kind of suggestions or improvements.