from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Jugador
from app.schemas import JugadorCreate, JugadorUpdate, JugadorRead
from app.database import get_db

router = APIRouter(prefix="/jugadores", tags=["Jugadores"])

@router.post("/", response_model=JugadorRead)
def crear_jugador(data: JugadorCreate, db: Session = Depends(get_db)):
    jugador = Jugador(**data.dict())
    db.add(jugador)
    db.commit()
    db.refresh(jugador)
    return jugador

@router.get("/", response_model=list[JugadorRead])
def obtener_jugadores(db: Session = Depends(get_db)):
    return db.query(Jugador).all()

@router.get("/{jugador_id}", response_model=JugadorRead)
def obtener_jugador(jugador_id: int, db: Session = Depends(get_db)):
    jugador = db.query(Jugador).filter(Jugador.id == jugador_id).first()
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return jugador

@router.put("/{jugador_id}", response_model=JugadorRead)
def actualizar_jugador(jugador_id: int, data: JugadorUpdate, db: Session = Depends(get_db)):
    jugador = db.query(Jugador).filter(Jugador.id == jugador_id).first()
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(jugador, key, value)
    db.commit()
    db.refresh(jugador)
    return jugador

@router.delete("/{jugador_id}")
def eliminar_jugador(jugador_id: int, db: Session = Depends(get_db)):
    jugador = db.query(Jugador).filter(Jugador.id == jugador_id).first()
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    db.delete(jugador)
    db.commit()
    return {"mensaje": "Jugador eliminado"}