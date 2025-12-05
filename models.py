from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'juagadores.db')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Jugador(Base):
       __tablename__ = "jugadores"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String(200), nullable=False)
    numero_camiseta = Column(int(100), unique=True, nullable=False, index=True)
    nacionalidad = Column(String(150),  nullable=False)
    fecha_nacimiento = Column(String(150), nullable=False)
    activo = Column(Boolean, default=True)

    altura = Column(int(500), nullable=False)
    peso = Column(int(100), nullable=False)
    pie_dominante = Column(String(100), nullable=False)
    posicion = Column(String(100), nullable=False)
    valor = Column(int(100), nullable=False)
    año_ingreso = Column(int(100), nullable=False)
    estado = Column(String(100), nullable=False)

    estadistica = relationship("Estadistica", back_populates="jugador")


class Estadistica():
       __tablename__ = "estadisticas"

    id = Column(Integer, primary_key=True, index=True)
    jugador_id = Column(Integer, ForeignKey("jugador.id"), nullable=True)
    tiempo_cancha = Column(int(100), nullable=False)
    numero_goles = Column(int(100), nullable=False)
    faltas = Column(int(100), nullable=False)
    targetas_resividas = Column(String(100), nullable=False)

    jugador = relationship("Jugador", back_populates="estadistica")
    


class Partido():
        __tablename__ = "partidos"

    id = Column(Integer, primary_key=True, index=True)
    jugador_id = Column(Integer, ForeignKey("jugador.id"), nullable=True)
    goles_equipo_sigFC = Column(String(100), nullable=False)
    goles_equipo_rival = Column(String(100), nullable=False)
    penales = Column(Boolean, default=True)
    npenales_gol_sigFc = Column(Boolean, default=True)
    npenales_gol_rival = Column(Boolean, default=True)
    resultado_partido = Column(String(100), nullable=False)

    partido = relationship("Jugador", back_populates="partido")


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()