# app/models/telemetry.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.config.database import DBBase

class Telemetry(DBBase):
    __tablename__ = 'telemetry'

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String(255), nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
