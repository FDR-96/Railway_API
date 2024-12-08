set -e

sleep 3 # Sleep 3 seconds for railway private URL to initialize

# Crear la base de datos si no existe
echo "Asegurando que la base de datos exista..."
python -m app.utils.db_utils  # Ejecutar db_utils.py como módulo

# Crear nuevas migraciones automáticamente si es necesario
echo "Generando migraciones de Alembic..."
if alembic revision --autogenerate -m "Auto migration"; then
    echo "Migraciones generadas exitosamente."
else
    echo "No se generaron nuevas migraciones."
fi

# Aplicar las migraciones a la base de datos
echo "Aplicando migraciones a la base de datos..."
alembic upgrade head

# Establecer PYTHONPATH y ejecutar la aplicación
echo "Iniciando la aplicación..."
export PYTHONPATH=$(pwd)
python -m app.main

# Iniciar el servidor
echo "Iniciando servidor..."
PORT=${PORT:-8000}  # Definir el puerto si no está en las variables de entorno
uvicorn app.main:app --host "0.0.0.0" --port $PORT
