# Flask Client, no usado para la presentación real,     

from flask import Flask, render_template
import pymysql
import paho.mqtt.client as mqtt
import json
from database import db

app = Flask(__name__)


# MQTT settings
mqtt_broker = "34.229.172.176"
mqtt_port = 1883
mqtt_topic = ["robertsen/feeds/temperatura","robertsen/feeds/humedad","robertsen/feeds/ppm","robertsen/feeds/batery"]


# Función que maneja los mensajes MQTT
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8"))
    topic_table = msg.topic.split("/")[-1]
    db.set_value(topic_table,payload)                

# Función para iniciar el cliente MQTT
def mqtt_connect(client):
    client.connect(mqtt_broker, mqtt_port, 60)
    client.loop_start()

# Ruta para la página principal que renderiza los datos con chart.js
@app.route('/')
def index():
    return render_template('index.html')
@app.route("/humedad")
def humedad():
    data = db.get_data_from_table("humedad")
    return data
@app.route("/temperatura")
def humedad():
    data = db.get_data_from_table("temperatura")
    return data
@app.route("/ppm")
def humedad():
    data = db.get_data_from_table("ppm")
    return data
        
@app.route("/batery")
def humedad():
    data = db.get_data_from_table("batery")
    return data
    

if __name__ == '__main__':
    # Configuración del cliente MQTT
    client = mqtt.Client()
    mqtt_connect(client)
    client.on_message = on_message

    # Suscripción a los tópicos
    for topic in mqtt_topic:
        client.subscribe(topic)

    app.run(debug=True)
