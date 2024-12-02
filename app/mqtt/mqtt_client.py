# app/mqtt/mqtt_client.py
import paho.mqtt.client as mqtt
from app.config.settings import get_settings

settings = get_settings()
# Configuración del cliente MQTT
MQTT_TOPIC = 'topic/test'

client = mqtt.Client()

def connect_mqtt():
    """Configura la conexión al broker MQTT"""
    client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, 60)

def on_connect(client, userdata, flags, rc):
    """Función que se ejecuta cuando el cliente se conecta al broker"""
    print(f"Conectado al broker MQTT con el código {rc}")
    client.subscribe(MQTT_TOPIC)

client.on_connect = on_connect
