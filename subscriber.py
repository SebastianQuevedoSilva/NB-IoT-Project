import paho.mqtt.client as mqtt
import math
from database import db
import time
import json

def on_connect(client,userdata,flags,rc):
    print("Subscriber conectado a mqtt" + str(rc))
    client.subscribe("robertsen/feeds/#") #se conecta a todos los topicos
    # client.subscribe("robertsen/feeds/temperatura")
    # client.subscribe("robertsen/feeds/humedad")
    # client.subscribe("robertsen/feeds/batery")
    # client.subscribe("robertsen/feeds/ppm")

def on_message(client, userdata, msg):
    print("Llegó un mensaje")
    payload = json.loads(msg.payload.decode("utf-8"))
    # print(payload,type(payload))
    topic_table = msg.topic.split("/")[-1]
    # print(topic_table)
    db.set_value(topic_table,payload)                


mqtt_broker = "34.229.172.176"
mqtt_port = 1883
mqtt_topic = ["/feeds/temperatura","/feeds/humedad","/feeds/ppm","/feeds/batery"]

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(mqtt_broker,mqtt_port,60)
client.loop_start()
time.sleep(2)

# for topic in mqtt_topic:
#     client.subscribe("robertsen"+topic)
#     time.sleep(1)
try:
    while True:
        time.sleep(30)
        # print("sigo escuchando")
except KeyboardInterrupt:
    # Disconnect on KeyboardInterrupt
    client.disconnect()
    client.loop_stop()
    print("Disconnected from MQTT broker.")
