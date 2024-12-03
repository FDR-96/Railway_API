# app/mqtt/mqtt_routes.py
from fastapi import APIRouter
from app.mqtt.mqtt_client import client

router = APIRouter()

#@router.on_event("startup")
 
@router.get("/publish/{message}")
async def publish_message(message: str):
    """Ruta para publicar un mensaje en un tópico MQTT"""
    client.publish('topic/test', message)
    return {"message": f"Mensaje '{message}' publicado en MQTT"}
