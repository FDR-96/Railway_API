# app/mqtt/mqtt_client.py
import json
import paho.mqtt.client as mqtt
from sqlalchemy.exc import SQLAlchemyError
from app.config.database import SessionLocal
from app.mqtt.models.telemetry import Telemetry
from app.config.settings import get_settings
from datetime import datetime


settings = get_settings()
MQTT_TOPIC = 'telemetry/#'

def get_db_session():
    """Crea y devuelve una sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def save_telemetry(telemetry, db_session):
#    """Guarda la telemetría en la base de datos"""
    try:
        db_session.add(telemetry)
        db_session.commit()
    except SQLAlchemyError as e:
        db_session.rollback()
        print(f"Error al guardar en la base de datos: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")

def on_message(client, userdata, message):
#    """Callback ejecutado al recibir un mensaje MQTT"""
    try:
        payload = json.loads(message.payload.decode())
        print(f"Received message on {message.topic}: {message.payload.decode()}")
        #print(f"Received message: {message}")
        device_id = payload.get("device_id")
        temperature = payload.get("temperature")
        humidity = payload.get("humidity")
        timestamp_str = payload.get("timestamp")
         
        if device_id and temperature and humidity and timestamp_str:
             # Asegúrate de que esta línea esté alineada correctamente (sin indentación extra)
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            
            telemetry = Telemetry(
                device_id=device_id,
                temperature=temperature,
                humidity=humidity,
                timestamp=timestamp,
            )
            db_session = next(get_db_session())
            save_telemetry(telemetry, db_session)
        else:
            print("Payload incompleto o inválido:", payload)
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
    except Exception as e:
        print(f"Error procesando el mensaje: {e}")

client = mqtt.Client()

def connect_mqtt():
    """Configura la conexión al broker MQTT"""
    print(settings.MQTT_BROKER)
    print(settings.MQTT_PORT)
    client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, 60)

def on_connect(client, userdata, flags, rc):
    """Función que se ejecuta cuando el cliente se conecta al broker"""
    print(f"Conectado al broker MQTT con el código {rc}")
    client.subscribe(MQTT_TOPIC)

def startup_mqtt():
    """Conectar al MQTT cuando arranque la aplicación"""
    connect_mqtt()
    client.loop_start()

client.on_connect = on_connect
client.on_message = on_message
