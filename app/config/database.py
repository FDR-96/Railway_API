# app/config/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from app.config.settings import get_settings

settings = get_settings()

engine = create_engine(
    url=settings.POSTGRES_DATABASE_URL,
    pool_pre_ping=True,
    pool_size=100,  # El tamaño del pool de conexiones
    max_overflow=50,  # El número máximo de conexiones que pueden abrirse por encima del tamaño del pool
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DBBase = declarative_base()

# Importa los modelos después de definir el engine
from app.mqtt.models.telemetry import Telemetry  # Importa solo después de configurar la base

# Crear las tablas si no existen
DBBase.metadata.create_all(bind=engine)
