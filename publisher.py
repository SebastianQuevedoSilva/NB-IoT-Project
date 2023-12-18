import paho.mqtt.client as mqtt
import math
import time
import json
def on_connect(client,userdata,flags,rc):
    print("Publisher conectado a mqtt" + str(rc))
    client.subscribe("robertsen/feeds/#") #se conecta a todos los topicos
    # client.subscribe("robertsen/feeds/temperatura")
    # client.subscribe("robertsen/feeds/humedad")
    # client.subscribe("robertsen/feeds/batery")
    # client.subscribe("robertsen/feeds/ppm")

def on_message(client,userdata,msg):
    print(msg.topic+" "+str(msg.payload))

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
data = {}
data['temperatura'] = ["{:.2f}".format(20+math.sin(2 * .31*math.pi*t)) for t in range(0,30,2)]
data['humedad'] = ["{:.2f}".format(abs( math.sin(2 * .31*math.pi*t))) for t in range(0,30,2)]
data['ppm'] = ["{:.2f}".format(600 +300*abs( math.sin(2 * .31*math.pi*t))) for t in range(0,30,2)]
data['batery'] = ["{:.2f}".format(math.exp(-t/100)) for t in range(0,30,2)]
try:
    while True:
        for key,values in data.items():
            time.sleep(60)
            for val in values:
                time.sleep(60)
                client.publish("robertsen/feeds/"+key,val)
except KeyboardInterrupt:
    # Disconnect on KeyboardInterrupt
    client.disconnect()
    client.loop_stop()
    print("Disconnected from MQTT broker.")
