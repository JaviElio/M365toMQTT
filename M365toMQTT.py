import json
import time
from m365py import m365py
from m365py import m365message
from paho.mqtt import client as mqtt_client

# MQTT
client = mqtt_client.Client('Raspi')
client.connect('192.168.xxx.xxx')

# M365
scooter_mac_address = 'XX:XX:XX:XX:XX:XX'
scooter = m365py.M365(scooter_mac_address, auto_reconnect=False)

try:

    scooter.connect()

    while True:
        # Request all currently supported 'attributes'
        scooter.request(m365message.battery_voltage)
        scooter.request(m365message.battery_ampere)
        scooter.request(m365message.battery_percentage)
        scooter.request(m365message.battery_cell_voltages)
        scooter.request(m365message.battery_info)

        scooter.request(m365message.general_info)
        scooter.request(m365message.motor_info)
        scooter.request(m365message.trip_info)
        scooter.request(m365message.trip_distance)
        scooter.request(m365message.distance_left)
        scooter.request(m365message.speed)
        scooter.request(m365message.tail_light_status)
        scooter.request(m365message.cruise_status)
        scooter.request(m365message.supplementary)

        # m365py also stores a cached state of received values
        client.publish("Patinete", json.dumps(scooter.cached_state, indent=4, sort_keys=True), retain=True)

        # Delay
        time.sleep(10)

except:
        print('Scooter not found or disconnected')


