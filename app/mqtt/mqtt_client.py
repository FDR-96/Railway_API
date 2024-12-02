# app/mqtt/mqtt_client.py
import paho.mqtt.client as mqtt

# Configuración del cliente MQTT
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'topic/test'

client = mqtt.Client()

def connect_mqtt():
    """Configura la conexión al broker MQTT"""
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

def on_connect(client, userdata, flags, rc):
    """Función que se ejecuta cuando el cliente se conecta al broker"""
    print(f"Conectado al broker MQTT con el código {rc}")
    client.subscribe(MQTT_TOPIC)

client.on_connect = on_connect
