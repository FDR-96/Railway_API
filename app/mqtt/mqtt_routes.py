# app/mqtt/mqtt_routes.py
from fastapi import APIRouter, Depends
from app.mqtt.mqtt_client import client
from app.auth.dependencies import get_current_user

router = APIRouter()

#@router.on_event("startup")
 
@router.get("/publish/{message}")
async def publish_message(message: str, current_user: str = Depends(get_current_user)):
    """Ruta para publicar un mensaje en un tópico MQTT"""
    client.publish('topic/test', message)
    return {"message": f"Mensaje '{message}' publicado en MQTT por {current_user}"}


