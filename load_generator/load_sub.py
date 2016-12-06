#!/usr/bin/env python

import paho.mqtt.client as mqtt
import sys
import time
import random


def on_message(client, userdata, message):
#    print "received:", message.payload
    pass

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

topic = "bg_load"

client = mqtt.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("server", 1883, 60)
client.subscribe(topic, 0)

running = True

while running:
    client.loop()
