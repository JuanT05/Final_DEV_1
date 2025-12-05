from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Jugador, Estadistica, Partido
from app.schemas import (
    JugadorCreate, JugadorUpdate, JugadorRead,
    EstadisticaCreate, EstadisticaUpdate, EstadisticaRead,
    PartidoCreate, PartidoUpdate, PartidoRead
)
from app.database import get_db


# ==============================
#       ROUTER ESTADISTICAS
# ==============================

router_estadisticas = APIRouter(prefix="/estadisticas", tags=["Estadísticas"])

@router_estadisticas.post("/", response_model=EstadisticaRead)
def crear_estadistica(data: EstadisticaCreate, db: Session = Depends(get_db)):
    estadistica = Estadistica(**data.dict())
    db.add(estadistica)
    db.commit()
    db.refresh(estadistica)
    return estadistica

@router_estadisticas.get("/", response_model=list[EstadisticaRead])
def obtener_estadisticas(db: Session = Depends(get_db)):
    return db.query(Estadistica).all()

@router_estadisticas.get("/{estadistica_id}", response_model=EstadisticaRead)
def obtener_estadistica(estadistica_id: int, db: Session = Depends(get_db)):
    estadistica = db.query(Estadistica).filter(Estadistica.id == estadistica_id).first()
    if not estadistica:
        raise HTTPException(status_code=404, detail="Estadística no encontrada")
    return estadistica

@router_estadisticas.put("/{estadistica_id}", response_model=EstadisticaRead)
def actualizar_estadistica(estadistica_id: int, data: EstadisticaUpdate, db: Session = Depends(get_db)):
    estadistica = db.query(Estadistica).filter(Estadistica.id == estadistica_id).first()
    if not estadistica:
        raise HTTPException(status_code=404, detail="Estadística no encontrada")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(estadistica, key, value)
    db.commit()
    db.refresh(estadistica)
    return estadistica

@router_estadisticas.delete("/{estadistica_id}")
def eliminar_estadistica(estadistica_id: int, db: Session = Depends(get_db)):
    estadistica = db.query(Estadistica).filter(Estadistica.id == estadistica_id).first()
    if not estadistica:
        raise HTTPException(status_code=404, detail="Estadística no encontrada")
    db.delete(estadistica)
    db.commit()
    return {"mensaje": "Estadística eliminada"}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Estadistica
from app.schemas import EstadisticaCreate, EstadisticaUpdate, EstadisticaRead
from app.database import get_db

router = APIRouter(prefix="/estadisticas", tags=["Estadísticas"])

@router.post("/", response_model=EstadisticaRead)
def crear_estadistica(data: EstadisticaCreate, db: Session = Depends(get_db)):
    estadistica = Estadistica(**data.dict())
    db.add(estadistica)
    db.commit()
    db.refresh(estadistica)
    return estadistica

@router.get("/", response_model=list[EstadisticaRead])
def obtener_estadisticas(db: Session = Depends(get_db)):
    return db.query(Estadistica).all()

@router.get("/{estadistica_id}", response_model=EstadisticaRead)
def obtener_estadistica(estadistica_id: int, db: Session = Depends(get_db)):
    estadistica = db.query(Estadistica).filter(Estadistica.id == estadistica_id).first()
    if not estadistica:
        raise HTTPException(status_code=404, detail="Estadística no encontrada")
    return estadistica

@router.put("/{estadistica_id}", response_model=EstadisticaRead)
def actualizar_estadistica(estadistica_id: int, data: EstadisticaUpdate, db: Session = Depends(get_db)):
    estadistica = db.query(Estadistica).filter(Estadistica.id == estadistica_id).first()
    if not estadistica:
        raise HTTPException(status_code=404, detail="Estadística no encontrada")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(estadistica, key, value)
    db.commit()
    db.refresh(estadistica)
    return estadistica

@router.delete("/{estadistica_id}")
def eliminar_estadistica(estadistica_id: int, db: Session = Depends(get_db)):
    estadistica = db.query(Estadistica).filter(Estadistica.id == estadistica_id).first()
    if not estadistica:
        raise HTTPException(status_code=404, detail="Estadística no encontrada")
    db.delete(estadistica)
    db.commit()
    return {"mensaje": "Estadística eliminada"}

