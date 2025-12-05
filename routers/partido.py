from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Partido
from app.schemas import PartidoCreate, PartidoUpdate, PartidoRead
from app.database import get_db

router = APIRouter(prefix="/partidos", tags=["Partidos"])

@router.post("/", response_model=PartidoRead)
def crear_partido(data: PartidoCreate, db: Session = Depends(get_db)):
    partido = Partido(**data.dict())
    db.add(partido)
    db.commit()
    db.refresh(partido)
    return partido

@router.get("/", response_model=list[PartidoRead])
def obtener_partidos(db: Session = Depends(get_db)):
    return db.query(Partido).all()

@router.get("/{partido_id}", response_model=PartidoRead)
def obtener_partido(partido_id: int, db: Session = Depends(get_db)):
    partido = db.query(Partido).filter(Partido.id == partido_id).first()
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return partido

@router.put("/{partido_id}", response_model=PartidoRead)
def actualizar_partido(partido_id: int, data: PartidoUpdate, db: Session = Depends(get_db)):
    partido = db.query(Partido).filter(Partido.id == partido_id).first()
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(partido, key, value)
    db.commit()
    db.refresh(partido)
    return partido

@router.delete("/{partido_id}")
def eliminar_partido(partido_id: int, db: Session = Depends(get_db)):
    partido = db.query(Partido).filter(Partido.id == partido_id).first()
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    db.delete(partido)
    db.commit()
    return {"mensaje": "Partido eliminado"}


#Estan bien?