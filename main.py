from fastapi import FastAPI
from models import Base
from database import engine
from routers.jugadores import router as jugadores_router
from routers.estadistica import router as estadisticas_router
from routers.partido import router as partidos_router

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SIG FC - Gestión de Jugadores", version="1.0")

# Incluir routers
app.include_router(jugadores_router)
app.include_router(estadisticas_router)
app.include_router(partidos_router)

@app.get("/")
def root():
    return {"mensaje": "API del equipo de fútbol funcionando correctamente"}
