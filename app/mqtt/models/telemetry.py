# app/mqtt/models/telemetry.py

from sqlalchemy import Column, Integer, String, Float, DateTime

def get_dbbase():
    from app.config.database import DBBase  # Importa aquí para evitar la importación circular
    return DBBase

class Telemetry(get_dbbase()):
    __tablename__ = 'telemetry'

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String(255), nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)

# No crees las tablas aquí directamente, lo haremos en el archivo de configuración
