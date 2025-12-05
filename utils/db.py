from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text, ForeignKey
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
    
    # Relación con datos_deportivos
    datos_Deportivos = relationship("Datos_Deportivos", back_populates="jugador")

class Datos_Deportivos(Base):
    __tablename__ = "datos_deportivos"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    altura = Column(int(500), nullable=False)
    peso = Column(int(100), nullable=False)
    pie_dominante = Column(String(100), nullable=False)
    posicion = Column(String(100), nullable=False)
    valor = Column(int(100), nullable=False)
    año_ingreso = Column(int(100), nullable=False)
    estado = Column(String(100), nullable=False)
    
    # Relación con jugadores
    usuario = relationship("Jugador", back_populates="datos_deportivos")
    

# Crear tablas
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()