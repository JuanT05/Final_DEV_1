from sqlalchemy.orm import Session
import models, schemas

# ----- JUGADORES -----
def crear_jugador(db: Session, jugador: schemas.JugadorCreate):
    db_jugador = models.Jugador(**jugador.dict())
    db.add(db_jugador)
    db.commit()
    db.refresh(db_jugador)
    return db_jugador

def listar_jugador(db: Session):
    return db.query(models.Jugador).all()

def obtener_jugador(db: Session, jugador_id: int):
    return db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()

def actualizar_jugador(db: Session, jugador_id: int, jugador_data: schemas.JugadorCreate):
    jugador = db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()
    if jugador:
        for key, value in jugador_data.dict().items():
            setattr(jugador, key, value)
        db.commit()
        db.refresh(jugador)
    return jugador

def eliminar_jugador(db: Session, jugador_id: int):
    jugador = db.query(models.Jugador).filter(models.Jugador.id == jugador_id).first()
    if jugador:
        db.delete(jugador)
        db.commit()
    return jugador


