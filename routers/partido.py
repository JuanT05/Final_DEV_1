from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_db
from models import Partido
from schemas import PartidoCreate, PartidoRead, PartidoUpdate

router = APIRouter(prefix="/partidos", tags=["Partidos"])



@router.get("/", response_model=list[PartidoRead])
def get_partidos(session: Session = Depends(get_db)):
    partidos = session.exec(select(Partido)).all()
    return partidos



@router.get("/{partido_id}", response_model=PartidoRead)
def get_partido(partido_id: int, session: Session = Depends(get_db)):
    partido = session.get(Partido, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return partido



@router.post("/", response_model=PartidoRead)
def create_partido(partido: PartidoCreate, session: Session = Depends(get_db)):
    nuevo_partido = Partido.model_validate(partido)
    session.add(nuevo_partido)
    session.commit()
    session.refresh(nuevo_partido)
    return nuevo_partido



@router.put("/{partido_id}", response_model=PartidoRead)
def update_partido(partido_id: int, data: PartidoUpdate, session: Session = Depends(get_db)):
    partido = session.get(Partido, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(partido, key, value)

    session.add(partido)
    session.commit()
    session.refresh(partido)
    return partido



@router.delete("/{partido_id}")
def delete_partido(partido_id: int, session: Session = Depends(get_db)):
    partido = session.get(Partido, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")

    session.delete(partido)
    session.commit()
    return {"message": "Partido eliminado correctamente"}
