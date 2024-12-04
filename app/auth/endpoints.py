from app.common.security import hash_password
from app.common.dependencies import get_db  # Asegúrate de tener una función para obtener la conexión a la BD
from app.config.settings import get_settings
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, APIRouter
from app.common.security import verify_password, create_access_token

settings = get_settings()
router = APIRouter()

@router.post("/register")
async def register_user(username: str, password: str, db=Depends(get_db)):
    hashed_password = hash_password(password)

    # Guardar el usuario en la base de datos (puedes personalizar esto según tu modelo)
    user = {"username": username, "password": hashed_password}
    db.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    db.commit()

    return {"message": "Usuario registrado exitosamente"}



@router.post("/login")
async def login_user(username: str, password: str, db=Depends(get_db)):
    # Buscar al usuario en la base de datos
    user = db.execute("SELECT * FROM users WHERE username = %s", (username,)).fetchone()
    if not user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

    # Verificar la contraseña
    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")

    # Crear el token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data = {"sub": username, "exp": datetime.utcnow() + access_token_expires}
    access_token = create_access_token(data=token_data)

    return {"access_token": access_token, "token_type": "bearer"}