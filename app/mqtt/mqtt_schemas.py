# app/mqtt/mqtt_schemas.py
from pydantic import BaseModel

class MqttMessage(BaseModel):
    topic: str
    message: str
