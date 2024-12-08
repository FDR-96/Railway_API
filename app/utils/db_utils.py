from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from config.settings import get_settings

def ensure_database_exists():
    """Crea la base de datos si no existe."""
    settings = get_settings()
    database_url = settings.POSTGRES_DATABASE_URL

    engine = create_engine(database_url)
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f"Base de datos creada: {database_url}")
    else:
        print(f"La base de datos ya existe: {database_url}")


if __name__ == "__main__":
    ensure_database_exists()
